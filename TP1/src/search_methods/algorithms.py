from collections import deque
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

    solution = reverseList(solution)
    return solution

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
                if n.getBoard().isSolved():
                    break
                children = n.getChildren()
                queue.append(children[0])

    solution = reverseList(solution)
    return solution

# Function for GREEDY
def greedy(visited, node, heuristic):
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
                if n.getBoard().isSolved():
                    break
                childPicked = childPicker(n.getChildren(), heuristic, 0)
                queue.append(childPicked)

    solution = reverseList(solution)
    return solution


# Function for A*
def astar(visited, node, heuristic):
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
                if n.getBoard().isSolved():
                    break
                childPicked = childPicker(n.getChildren(), heuristic, 1)
                queue.append(childPicked)
                
    solution = reverseList(solution)
    return solution