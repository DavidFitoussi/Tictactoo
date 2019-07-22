from Resource import clsResource
from enum import Enum

class Direction(Enum):
    Row = 1
    Column = 2
    DiagonalX = 3
    DiagonalY = 4

class clsGame:
    def __init__(self):
        self.InstanceResource = clsResource()
        self.MatrixArray = []
        self.CurrentSign = ' '
        
    def InitMatrix(self):
        for x in range(0, self.InstanceResource.MatrixSize):
            list = []
            self.MatrixArray.append(list)
        for x in range(0, self.InstanceResource.MatrixSize):
            for y in range(0, self.InstanceResource.MatrixSize):
                self.MatrixArray[x].append(' ')
    def Clear(self):
        for x in range(0, self.InstanceResource.MatrixSize):
            for y in range(0, self.InstanceResource.MatrixSize):
                self.MatrixArray[x - 1][y - 1] = ' '


    def SetPosition(self,Sign,x,y):
        self.CurrentSign = Sign
        if (self.MatrixArray[x-1][y-1] == ' '):
            self.MatrixArray[x - 1][y - 1] = Sign
            return True
        else: return False

    def IsWinner(self):
        return (self.DirectionCheck(Direction.Row) or
                self.DirectionCheck(Direction.Column) or
                self.DirectionCheck(Direction.DiagonalX) or
                self.DirectionCheck(Direction.DiagonalY)
                  )

    def DirectionCheck(self,direction):
        Counter = 0
        for x in range(0, self.InstanceResource.MatrixSize):
            if (direction != Direction.DiagonalY) and (direction != Direction.DiagonalX):
                Counter = 0
            for y in range(0, self.InstanceResource.MatrixSize):
                if (
                    ((direction == Direction.Row) and (self.MatrixArray[x-1][y-1] == self.CurrentSign)) or
                    ((direction == Direction.DiagonalX) and (self.MatrixArray[x - 1][x - 1] == self.CurrentSign) and (x==y)) or
                    ((direction == Direction.DiagonalY) and (self.MatrixArray[self.InstanceResource.MatrixSize -x - 1][y] == self.CurrentSign) and (x == y)) or
                    ((direction == Direction.Column) and (self.MatrixArray[y - 1][x - 1] == self.CurrentSign))
                ):
                    Counter += 1
                    if (Counter == self.InstanceResource.MatrixSize):
                        return True
        return False




        
        
        
    
