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

    def hasSameColor(self, Squeare):
        return self.squareColor == Squeare.squareColor

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