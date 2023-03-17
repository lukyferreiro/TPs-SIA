class Node:

    def __init__(self, board, parent):
        self.board = board
        self.children = []
        self.parent = parent

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def processChildren(self):
        if not self.board.isSolved():
            colorDict = self.board.getColorDict()

            for colorName in colorDict.keys():
                if self.board.getPlayerColor() != colorDict[colorName]:

                    newState = self.board.getStateCopy()
                    newState.changeColor(colorName)

                    # Solo seguimos explorando el nodo si hubo un cambio en la cantidad de cuadrados que controla el jugador
                    # Sino, podríamos analizar infinitamente cambios de 1 color a otro:
                    # EJ numérico:
                    # 1 2    3 2    1 2    3 2
                    # 2 3 -> 2 3 -> 2 3 -> 2 3
                    if self.gameState.getPlayerCount() < newState.getPlayerCount():
                        newNode = Node(newState, self)
                        self.children.append(newNode)

    def getChildren(self):
        if len(self.children) == 0 and not self.board.isSolved():
            self.processChildren()
        return self.children

    def getParent(self):
        return self.parent

    def getPlayerCount(self):
        return self.board.getPlayerCount()

    def getPlayerColor(self):
        return self.board.getPlayerColor()

    def printNode(self):
        self.board.printState()

    def getBoard(self):
        return self.board

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.gameState.printState()

    def isUseful(self, node):
        return self.gameState.getPlayerCount() < node.gameState.getPlayerCount()