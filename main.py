from Game import clsGame
from Resource import  clsResource
import os

# This is a sample of TicTactoo game .
# you can configure 2 parameters in config.py file config :
# 1. MatrixSize is the number of line/column of the matrix
# 2. 2 players game ( ComputerPlayer : False ) or playing with the computer ( ComputerPlayer: True)
#
# Run the main.py to start ....

# main fuunctions ...
def Print():
    underline = ""
    for z in range(0, InstanceResource.MatrixSize):
        underline += "==="
    line = ""
    for x in range(0, InstanceResource.MatrixSize):
        for y in range(0, InstanceResource.MatrixSize):
            line += InstanceGame.MatrixArray[x][y] + (" | " if y < InstanceResource.MatrixSize -1 else "")
        print(line)
        line =""
        if (x < InstanceResource.MatrixSize -1 ):
            print(underline)

def InputNumber(caption):
    x = "0"
    while (True) :
        x = str(input("Please enter the {} number:".format(caption)))
        if (not(x.isdigit())) :
            print("Incorrect input.Please enter a number...")
        else : break
    return int(x)

# Here the code starts ...
InstanceResource = clsResource()
loopnumber = 0
InstanceGame = clsGame()
InstanceGame.InitMatrix()

CurrentSign = 'X'
IsGameOver = False

while (loopnumber < InstanceResource.MatrixSize * InstanceResource.MatrixSize) and (IsGameOver == False):
    Print()
    IsCorrectSet = True
    while IsCorrectSet == True:
        CurrentSign = "X" if (loopnumber % 2 == 0) else "0"
        print('Player {}\n'.format(CurrentSign))
        if (CurrentSign == "0") and (InstanceResource.ComputerPlayer == True):
            ComputerPosition = InstanceGame.GetRandomFreePlace()
            x = ComputerPosition[0]
            y = ComputerPosition[1]
        else :
            x = InputNumber("Line")
            y = InputNumber("Column")
        IsCorrectSet = InstanceGame.SetPosition(CurrentSign,x,y)
        if (IsCorrectSet == False):
            print("[{},{}] is busy.Try again...".format(x,y))
        else:
            loopnumber += 1
        if (InstanceGame.IsWinner()==True):
            Print()
            print("{} IS WIN !!!!!".format(CurrentSign))
            print('Play again ?(y/n):')
            if (input() == 'n'):
                IsGameOver = True
                break
            else:
                InstanceGame.Clear()
                loopnumber= 0
        else:
            print("Next player")
        Print()

print("Game over")

