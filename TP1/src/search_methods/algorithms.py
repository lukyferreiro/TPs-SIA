from src.search_methods.heuristics import childPicker

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
    queue = [node]
    solved = False

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
    solved = False

    while not solved:
        n = queue.pop(0)

        if n.getBoard().isSolved():
            solved = True
        else:
            if n not in visited:
                visited.append(n)
                if n.getBoard().isSolved():
                    break
                children = n.getChildren()
                queue.append(children[0])

    return visited

# Function for GREEDY
def greedy(visited, node, heuristic):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getBoard().isSolved():
                break
            childPicked = childPicker(n.getChildren(), heuristic, 0)
            queue.append(childPicked)


# Function for A*
def astar(visited, node, heuristic):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getBoard().isSolved():
                break
            childPicked = childPicker(n.getChildren(), heuristic, 1)
            queue.append(childPicked)