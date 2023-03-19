from src.game_state.square import square

def childPicker(children, heuristic, edgeWeight):
    neighborValues = []
    EDGE_WEIGHT = edgeWeight
    for neighbor in children:
        if heuristic == 'Remainig colors':
            neighborValue = remainingColorsHeuristic(neighbor)
        if heuristic == 'Most neighbors':
            neighborValue = mostNeighborsHeuristic(neighbor)
        neighborValues.append(neighborValue)

    minValue = neighborValues[0] + EDGE_WEIGHT  # get MinValue neighbor
    index = 0
    for i in range(len(neighborValues) - 1):
        if neighborValues[i + 1] + EDGE_WEIGHT < minValue:
            index = i + 1
            minValue = neighborValues[i + 1] + EDGE_WEIGHT

    return children[index]
    
def mostNeighborsHeuristic(neighbor):
    totalSquares = neighbor.getBoard().N ** 2
    return totalSquares - neighbor.getBoard().getPlayerCount()

def remainingColorsHeuristic(neighbor):
    colorValues = neighbor.getBoard().getColorDict().values()
    colorSeen = []
    for square in neighbor.getBoard().looseSquares:
        if len(colorSeen) == len(colorValues):
            break
        if square.squareColor not in colorSeen:
            colorSeen.append(square.squareColor)

    return len(colorSeen)