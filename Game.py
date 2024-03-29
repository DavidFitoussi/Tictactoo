from Resource import clsResource
from enum import Enum
import random


# Direction Enum used to check the different direction of line winner 
class Direction(Enum):
    Row = 1
    Column = 2
    DiagonalX = 3
    DiagonalY = 4

class clsGame:
    # constructor of Game , initialize the local variables
    # Matrixarray is multiple array of list [[],[],[]] 
    # FreePlaces is the list of the free place in the array , needed for computer player whitch choose his random number in this list  
    def __init__(self):
        self.InstanceResource = clsResource() 
        self.MatrixArray = []
        self.FreePlaces  =[]
        self.CurrentSign = ' '
        
    # initialize the matrix according to the size of matrix from the configuration 
    def InitMatrix(self):
        for x in range(0, self.InstanceResource.MatrixSize):
            list = []
            self.MatrixArray.append(list)
        for x in range(0, self.InstanceResource.MatrixSize):
            for y in range(0, self.InstanceResource.MatrixSize):
                self.MatrixArray[x].append(' ')
                self.FreePlaces.append([x +1,y +1])

    def Clear(self):
        self.FreePlaces = []
        for x in range(0, self.InstanceResource.MatrixSize):
            for y in range(0, self.InstanceResource.MatrixSize):
                self.MatrixArray[x - 1][y - 1] = ' '
                self.FreePlaces.append([x + 1, y + 1])



    def SetPosition(self,Sign,x,y):
        self.CurrentSign = Sign
        if (self.MatrixArray[x-1][y-1] == ' '):
            self.MatrixArray[x - 1][y - 1] = Sign
            xToRemove = x
            yToRemove = y
            list = [xToRemove,yToRemove]
            #print("set position {} and remove from Free place {}".format(list, self.FreePlaces))
            self.FreePlaces.remove([xToRemove,yToRemove])
            #print("After set position ,Free place are ", self.FreePlaces)
            return True
        else: return False

    # Return a couple of position x,y get from freeplace array , when the position in the list is get by random function 
    def GetRandomFreePlace(self):
        x= random.randint(1,len(self.FreePlaces))
        return self.FreePlaces[x -1]

    # Check all the posibility of a "full line" to win the game  
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




        
        
        
    
