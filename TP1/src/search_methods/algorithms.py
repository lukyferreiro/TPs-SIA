from collections import deque
from src.search_methods.heuristics import greedyChildPicker, heuristicCalculator
from src.utils import currentMilliTime


def chooseAlgorithm(algorithm_type, heuristic, solution, visited, rootNode, time):
    match algorithm_type:
            case 'BFS':
                t0 = currentMilliTime()
                solution, visited = bfs(visited, rootNode)
                time = currentMilliTime() - t0
            case 'DFS':
                t0 = currentMilliTime()
                solution, visited = dfs(visited, rootNode)
                time = currentMilliTime() - t0
            case 'GREEDY':
                t0 = currentMilliTime()
                solution, visited = greedy(visited, rootNode, heuristic)
                time = currentMilliTime() - t0
            case 'A*':
                t0 = currentMilliTime()
                solution, visited = astar(visited, rootNode, heuristic)
                time = currentMilliTime() - t0
    return solution, visited, time

def traceBack(node, solution):
    queue = [node]
    while queue:
        m = queue.pop(0)
        solution.append(m)
        if m.getParent() is None:
            break
        else:
            queue.append(m.getParent())

# Function for BFS
def bfs(visited, node):  
    solution = []
    queue = deque([node])
    solved = False
    visited.add(node) # initialize visited as a set

    while queue and not solved:
        n = queue.popleft()
        if n.getBoard().isSolved():
            traceBack(n, solution)
            solved = True
        else:
            children = n.getChildren()
            for child in children:
                if n.isUseful(child) and child not in visited: # use "not in visited" instead of "child not in visited"
                    queue.append(child)
                    visited.add(child) # add child to visited using the "add" method of a set

    solution.reverse()
    return solution, visited

# Function for DFS
def dfs(visited, node):
    solution = []
    queue = deque([node])
    solved = False

    while not solved:
        n = queue.popleft()
        if n.getBoard().isSolved():
            traceBack(n, solution)
            solved = True
        else:
            if n not in visited:
                visited.add(n)

            children = n.getChildren()
            queue.append(children[0])

    solution.reverse()
    return solution, visited

# Function for GREEDY
def greedy(visited, node, heuristic):
    solution = []
    queue = deque([node])
    solved = False

    while queue and not solved:
        n = queue.popleft()
        if n.getBoard().isSolved():
            traceBack(n, solution)
            solved = True
        else:
            if n not in visited:
                visited.add(n)

            childPicked = greedyChildPicker(n.getChildren(), heuristic)
            queue.append(childPicked)

    solution.reverse()
    return solution, visited


# Function for A*
def astar(visited, start_node, heuristic):
    solved = False
    solution = []

    #Costo de llegar
    start_node.g_cost = 0
    #Costo heuristica (h_cost)
    start_node.f_cost = heuristicCalculator(heuristic, start_node)
    current_node = None

    frontier = [start_node]
    visited.add(start_node)

    while not solved and frontier:
        current_node = frontier[0]

        for node in frontier:
            if node.f_cost < current_node.f_cost:
                 visited.add(current_node)
                 current_node = node
            elif node.f_cost == current_node.f_cost and node.g_cost < current_node.g_cost:
                visited.add(current_node)
                current_node = node
            else:
                frontier.remove(node)

        if current_node.getBoard().isSolved():
            traceBack(current_node, solution)
            solved = True
        else:
            visited.add(current_node)

            children = current_node.getChildren()

            for child in children:
                if child not in visited:
                    new_cost = current_node.g_cost + 1

                    if child not in frontier:
                        child.g_cost = new_cost
                        child.f_cost = child.g_cost + heuristicCalculator(heuristic, child)
                        frontier.append(child)

    solution.reverse()
    return solution, visited