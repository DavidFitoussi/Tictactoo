from Game import clsGame
from Resource import  clsResource


def Print():
    underline = ""
    for z in range(0, InstanceResource.MatrixSize):
        underline += "---"
    line = ""
    for x in range(0, InstanceResource.MatrixSize):
        for y in range(0, InstanceResource.MatrixSize):
            line += InstanceGame.MatrixArray[x][y] + (" | " if y < InstanceResource.MatrixSize -1 else "")
        print(line)
        line =""
        if (x < InstanceResource.MatrixSize -1 ):
            print(underline)


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
        print('Player {}\nLine number:'.format(CurrentSign))
        x = int(input())
        print('Column number:')
        y = int(input())
        IsCorrectSet = InstanceGame.SetPosition(CurrentSign,x,y)
        if (IsCorrectSet == False):
            print("[{},{}] is busy.Try again...".format(x,y))
        else:
            print("Next player")
            loopnumber += 1
        Print()
        if (InstanceGame.IsWinner()==True):
            print("{} IS WIN !!!!!".format(CurrentSign))
            print('Play again ?(y/n):')
            if (input() == 'n'):
                IsGameOver = True
                break
            else:
                InstanceGame.Clear()
                loopnumber= 0
                Print()


print("Game over")

