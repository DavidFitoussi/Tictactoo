from Game import clsGame
from Resource import  clsResource


def Print():
    underline = ""
    for z in range(0, InstanceResource.MatrixSize):
        underline += "--"
    line = ""
    for x in range(0, InstanceResource.MatrixSize):
        for y in range(0, InstanceResource.MatrixSize):
            line += InstanceGame.MatrixArray[x][y] + ("|" if y < InstanceResource.MatrixSize -1 else "")
        print(line)
        line =""
        if (x < InstanceResource.MatrixSize -1 ):
            print(underline)

InstanceGame = clsGame()
InstanceResource = clsResource()
InstanceGame.InitMatrix()
loopnumber = 0
CurrentSign = 'X'
Print()
while loopnumber < InstanceResource.MatrixSize * InstanceResource.MatrixSize:
    CurrentSign = "X" if (loopnumber % 2 == 0) else "0"
    print('Player {}\nLine number:'.format(CurrentSign))
    x = int(input())
    print('Column number:')
    y = int(input())

    loopnumber += 1
    InstanceGame.SetPosition(CurrentSign,x,y)
    Print()
    if (InstanceGame.IsWinner()==True):
        break
print("Game over")

