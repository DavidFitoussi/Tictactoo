from Resource import clsResource


class clsGame:
    def __init__(self):
        self.InstanceResource = clsResource()
        self.MatrixArray = [[],[],[]]
        self.CurrentSign = '_'
        
    def InitMatrix(self):
        for x in range(0, self.InstanceResource.MatrixSize):
            for y in range(0, self.InstanceResource.MatrixSize):
                self.MatrixArray[x].append("_")
        self.Print()
    
    def Print(self):
        for x in range(0, self.InstanceResource.MatrixSize):
            print(self.MatrixArray[x])

    def SetPosition(self,Sign,x,y):
        self.CurrentSign = Sign
        self.MatrixArray[x-1][y-1]= Sign
        self.Print()
        
    def IsWinner(self):
        # self.LineCheck()
        self.ColumnCheck()
        
    def LineCheck(self):
        IsWin = False 
        for x in range(0, self.InstanceResource.MatrixSize):
            Counter = 0
            for y in range(0, self.InstanceResource.MatrixSize):
                if (self.MatrixArray[x-1][y-1] == self.CurrentSign):
                    Counter += 1
                    if (Counter == self.InstanceResource.MatrixSize):
                        IsWin == True
                        print("{} is win !!!!!",self.CurrentSign)
                        
    def ColumnCheck(self):
        IsWin = False
        for x in range(0, self.InstanceResource.MatrixSize):
            Counter = 0
            for y in range(0, self.InstanceResource.MatrixSize):
                if (self.MatrixArray[x-1][y-1] == self.CurrentSign):
                    Counter += 1
                    if (Counter == self.InstanceResource.MatrixSize):
                        IsWin == True
                        print("{} is win !!!!!",self.CurrentSign)
                        break
                else :
                    Counter = 0
                    break

        
        
        
    
