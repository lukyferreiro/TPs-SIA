import networkx as nx
from src.game_state.square import square

def childPicker(children, heuristic, edgeWeight):
    childValues = []
    EDGE_WEIGHT = edgeWeight
    for child in children:
        if heuristic == 'Remaining colors':
            childValue = remainingColorsHeuristic(child)
        if heuristic == 'Most neighbors':
            childValue = mostNeighborsHeuristic(child)
        if heuristic == 'Bronson distance':
            childValue = bronsonHeuristic(child)
        childValues.append(childValue)

    # Gey min value child
    minValue = childValues[0] + EDGE_WEIGHT  
    index = 0
    for i in range(len(childValues) - 1):
        if childValues[i + 1] + EDGE_WEIGHT < minValue:
            index = i + 1
            minValue = childValues[i + 1] + EDGE_WEIGHT

    return children[index]
    
def mostNeighborsHeuristic(child):
    totalSquares = child.getBoard().N ** 2
    return totalSquares - child.getBoard().getPlayerCount()

def remainingColorsHeuristic(child):
    colorValues = child.getBoard().getColorDict().values()
    colorSeen = []
    for square in child.getBoard().looseSquares:
        if len(colorSeen) == len(colorValues):
            break
        if square.squareColor not in colorSeen:
            colorSeen.append(square.squareColor)

    return len(colorSeen)

def bronsonHeuristic(child):
    DISTANCE = 0
    state = child.getBoard()
    playerSquare = square(state.N + 1, state.N + 1, 0,
                      True)  # this squeare does not exist in board and represents all player squares in graph
    graph = generateBronsonGraph(child.getBoard(), playerSquare)
    len_path = dict(nx.all_pairs_dijkstra(graph))
    maxValue = 0
    for key in len_path[playerSquare][DISTANCE]:
        if len_path[playerSquare][DISTANCE][key] > maxValue:
            maxValue = len_path[playerSquare][DISTANCE][key]
    return maxValue

def generateBronsonGraph(state, playerSquare):
    board = state.getBoard()
    graph = nx.Graph()
    graph.add_node(playerSquare)
    for i in range(state.N):
        for j in range(state.N):
            square = board[i][j]
            if not square.getIsPlayer():
                graph.add_node(square)
                if square.hasTop():
                    top = board[square.x - 1][square.y]
                    graph.add_node(top)
                    if top.getIsPlayer():
                        graph.add_edge(playerSquare, square, weight=1)
                    elif square.hasSameColor(top):
                        graph.add_edge(square, top, weight=0)
                    else:
                        graph.add_edge(square, top, weight=1)

                if square.hasLeft():
                    left = board[square.x][square.y - 1]
                    graph.add_node(left)
                    if left.getIsPlayer():
                        graph.add_edge(playerSquare, square, weight=1)
                    elif square.hasSameColor(left):
                        graph.add_edge(square, left, weight=0)
                    else:
                        graph.add_edge(square, left, weight=1)

                if square.hasRight(state.N):
                    right = board[square.x][square.y + 1]
                    graph.add_node(right)
                    if right.getIsPlayer():
                        graph.add_edge(playerSquare, square, weight=1)
                    elif square.hasSameColor(right):
                        graph.add_edge(square, right, weight=0)
                    else:
                        graph.add_edge(square, right, weight=1)

                if square.hasDown(state.N):
                    down = board[square.x + 1][square.y]
                    graph.add_node(down)
                    if down.getIsPlayer():
                        graph.add_edge(playerSquare, square, weight=1)
                    elif square.hasSameColor(down):
                        graph.add_edge(square, down, weight=0)
                    else:
                        graph.add_edge(square, down, weight=1)
    return graph