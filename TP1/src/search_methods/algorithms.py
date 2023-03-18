from src.game_state.square import square

def bfs(visited, node):  # function for BFS
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

    # Retorna la solución de estados a correr.
    queue.clear()
    solution = reverseList(solution)
    return solution

def dfs(visited, node):
    queue = [node]

    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getBoard().isSolved():
                break
            children = n.getChildren()
            queue.append(children[0])  # all neighbors can reach solution so I can choose any neighbor I want

    return visited

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