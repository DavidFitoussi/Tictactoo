from Game import clsGame
from Resource import  clsResource


InstanceGame = clsGame()
InstanceResource = clsResource()
InstanceGame.InitMatrix()
loopnumber = 0
CurrentSign = 'X'
while loopnumber < InstanceResource.MatrixSize * InstanceResource.MatrixSize:
    print('X Position:')
    x = int(input())
    print('Y Position:')
    y = int(input())
    CurrentSign = "X" if (loopnumber % 2 == 0) else "0"
    loopnumber += 1
    InstanceGame.SetPosition(CurrentSign,x,y)
    InstanceGame.IsWinner()


