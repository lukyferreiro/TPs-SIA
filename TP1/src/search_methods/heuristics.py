def childPicker(children, heuristic, edgeWeight):
    childValues = []
    EDGE_WEIGHT = edgeWeight
    for child in children:
        if heuristic == 'Remainig colors':
            neighborValue = remainingColorsHeuristic(child)
        if heuristic == 'Most neighbors':
            neighborValue = mostNeighborsHeuristic(child)
        childValues.append(neighborValue)

    minValue = childValues[0] + EDGE_WEIGHT  # get MinValue child
    index = 0
    for i in range(len(childValues) - 1):
        if childValues[i + 1] + EDGE_WEIGHT < minValue:
            index = i + 1
            minValue = childValues[i + 1] + EDGE_WEIGHT

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