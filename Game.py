from Resource import clsResource
from enum import Enum

class Direction(Enum):
    Row = 1
    Column = 2
    Diagonal = 3

class clsGame:
    def __init__(self):
        self.InstanceResource = clsResource()
        self.MatrixArray = [[],[],[]]
        self.CurrentSign = ' '
        
    def InitMatrix(self):
        for x in range(0, self.InstanceResource.MatrixSize):
            for y in range(0, self.InstanceResource.MatrixSize):
                self.MatrixArray[x].append(" ")
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
                  self.DirectionCheck(Direction.Diagonal)
                  )

    def DirectionCheck(self,direction):
        for x in range(0, self.InstanceResource.MatrixSize):
            Counter = 0
            for y in range(0, self.InstanceResource.MatrixSize):
                if (((direction.Row) and (self.MatrixArray[x-1][y-1] == self.CurrentSign)) or
                   # ((direction.Diagonal) and (self.MatrixArray[x - 1][x - 1] == self.CurrentSign)) or
                    ((direction.Column) and (self.MatrixArray[y - 1][x - 1] == self.CurrentSign))):
                    Counter += 1
                    if (Counter == self.InstanceResource.MatrixSize):
                        return True
        return False




        
        
        
    
