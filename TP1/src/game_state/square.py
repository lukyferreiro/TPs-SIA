class square:

    def __init__(self, x, y, squareColor, isPlayer):
        self.x = x
        self.y = y
        self.isPlayer = isPlayer
        self.squareColor = squareColor

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y and self.squareColor == other.squareColor and self.isPlayer == other.isPlayer

    def setColor(self, squareColor):
        self.squareColor = squareColor

    def getColor(self):
        return self.squareColor

    def hasSameColor(self, Square):
        return self.squareColor == Square.squareColor

    def setIsPlayer(self, isPlayer):
        self.isPlayer = isPlayer

    def getIsPlayer(self):
        return self.isPlayer

    def hasRight(self, maxValueX):
        return self.y < maxValueX - 1

    def hasTop(self):
        return self.x > 0

    def hasLeft(self):
        return self.y > 0

    def hasDown(self, maxValueX):
        return self.x < maxValueX - 1

    def isBorder(self, board, N):
        top = True
        right = True
        down = True
        left = True

        if self.hasTop():
            top = board[self.x - 1][self.y].getIsPlayer()

        if self.hasRight(N):
            right = board[self.x][self.y + 1].getIsPlayer()

        if self.hasDown(N):
            down = board[self.x + 1][self.y].getIsPlayer()

        if self.hasLeft():
            left = board[self.x][self.y - 1].getIsPlayer()

        return not (top and right and down and left)