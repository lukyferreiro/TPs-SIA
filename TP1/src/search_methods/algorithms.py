from src.search_methods.heuristics import neighborPicker

def traceBack(node, solution):
    queue = [node]
    while queue:
        m = queue.pop(0)
        solution.append(m)
        if m.getParent() is None:
            break
        else:
            queue.append(m.getParent())

def reverseList(solution):
    reversed = []
    for node in solution:
        reversed.insert(0, node)
    return reversed

# Function for BFS
def bfs(visited, node):  
    solution = []
    queue = []
    solved = False

    queue.append(node)
    visited.append(node)

    while queue and not solved:  # Creating loop to visit each node
        m = queue.pop(0)
        if m.getBoard().isSolved():
            traceBack(m, solution)
            solved = True
        else:
            children = m.getChildren()
            for child in children:
                if m.isUseful(child) and child not in visited:
                    queue.append(child)
                    visited.append(child)

    queue.clear()
    solution = reverseList(solution)
    return solution # Returns solutios with all states

# Function for DFS
def dfs(visited, node):
    queue = [node]

    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getBoard().isSolved():
                break
            children = n.getChildren()
            queue.append(children[0])  # All neighbors can reach solution so I can choose any neighbor I want

    return visited

# Function for GREEDY
def greedy(visited, node, option):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getBoard().isSolved():
                break
            neighborPicked = neighborPicker(n.getNeighbors(), option, 0)
            queue.append(neighborPicked)


# Function for A*
def astar(visited, node, option):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getBoard().isSolved():
                break
            neighborPicked = neighborPicker(n.getNeighbors(), option, 1)
            queue.append(neighborPicked)