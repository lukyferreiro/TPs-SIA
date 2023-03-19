import numpy as np
import random
import copy
from src.game_state.square import square

class Board:

    def __init__(self, N, colors):
        self.playerColor = None
        self.N = N
        self.board = [[] for _ in range(N)]
        self.playerSquares = []
        self.looseSquares = []
        self.colorList = dict(colors)
        for i in range(N):
            for j in range(N):
                newColor = random.choice(list(self.colorList.values()))
                if i == 0 and j == 0:
                    self.board[i].append(square(i, j, newColor, True))
                    self.playerColor = newColor
                    self.playerSquares.append(self.board[i][j])
                    self.board[i][j].setIsPlayer(True)
                else:
                    square_aux = square(i, j, newColor, False)
                    self.board[i].append(square_aux)
                    self.looseSquares.append(square_aux)

        self.addSquares()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.playerColor != other.playerColor or len(self.playerSquares) != len(other.playerSquares):
            return False
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True

    def __hash__(self):
        return hash((len(self.playerSquares), self.playerColor))

    def getSquare(self, x, y):
        return self.board[x][y]

    def changeColor(self, color):
        colorToChange = self.colorList[color]
        self.playerColor = colorToChange
        for cell in self.playerSquares:
            cell.setColor(colorToChange)

        self.addSquares()

    def getPlayerColor(self):
        return self.playerColor

    def isSolved(self):
        return len(self.playerSquares) == self.N * self.N

    def addSquares(self):
        for square in self.playerSquares:
            if square.hasTop():
                top = self.board[square.x - 1][square.y]
                if not top.getIsPlayer() and square.hasSameColor(top):
                    top.setIsPlayer(True)
                    self.playerSquares.append(top)
                    self.looseSquares.remove(top)
            if square.hasRight(self.N):
                right = self.board[square.x][square.y + 1]
                if not right.getIsPlayer() and square.hasSameColor(right):
                    right.setIsPlayer(True)
                    self.playerSquares.append(right)
                    self.looseSquares.remove(right)
            if square.hasDown(self.N):
                down = self.board[square.x + 1][square.y]
                if not down.getIsPlayer() and square.hasSameColor(down):
                    down.setIsPlayer(True)
                    self.playerSquares.append(down)
                    self.looseSquares.remove(down)
            if square.hasLeft():
                left = self.board[square.x][square.y - 1]
                if not left.getIsPlayer() and square.hasSameColor(left):
                    left.setIsPlayer(True)
                    self.playerSquares.append(left)
                    self.looseSquares.remove(left)

    def getStateCopy(self):
        return copy.deepcopy(self)

    def getPlayerCount(self):
        return len(self.playerSquares)

    def getColorValue(self, colorName):
        return self.colorList[colorName]

    def getColorDict(self):
        return self.colorList

    def getBoard(self):
        return self.board

    def getLooseSquares(self):
        return self.looseSquares