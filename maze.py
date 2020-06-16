from turtle import *
from random import randrange

# 처음 시작 포인트 좌표입니다
startPoint = [-275, 275]

# 처음 미로를 테두리를 세팅해줍니다
setup(600, 600)
hideturtle()
speed(1000000)
penup()
goto(-275, 275)
showturtle()
pendown()
goto(-275, -275)
goto(275, -275)
goto(275, 275)
goto(-275, 275)

# 장애물 위치를 구현한 Nested array, 실제 장애물 위치가 아닙니다
obstacles = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 3],
             [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 3],
             [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 3],
             [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 3],
             [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 3],
             [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 3],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3],
             [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 3],
             [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 3],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 3],
             [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 3]]

# 장애물을 그려주기 위한 함수입니다
def drawObstacle():
    color("red")
    begin_fill()
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    end_fill()
    forward(50)


# 미로를 그려주기 위한 함수입니다
def drawMap():
    for i in obstacles:
        for j in i:
            if j == 0:
                penup()
                forward(50)
                pendown()
            elif j == 3:
                startPoint[1] = startPoint[1] - 50
                penup()
                goto(startPoint[0], startPoint[1])
                pendown()
            else:
                drawObstacle()


image = {'right': 'right.gif', 'left': 'left.gif', 'up': 'up.gif', 'down': 'down.gif'}


# 팩맨을 세팅해주는 함수입니다
def setUpPacman():
    # gem을 설정해줍니다
    turtle2 = Turtle()
    turtle2.hideturtle()
    gem = {"gem": "gem.gif"}
    addshape("gem.gif")
    turtle2.shape(gem["gem"])
    turtle2.penup()
    turtle2.goto(250, -250)
    turtle2.showturtle()

    penup()
    goto(-250, 250)
    addshape(image["up"])
    addshape(image["down"])
    addshape(image["left"])
    addshape(image["right"])
    shape(image["right"])


# 장애물의 위치입니다
block_position = ((-150, 250), (-100, 250), (0, 250), (150, 250),
                  (-250, 200), (-100, 200), (0, 200), (100, 200), (150, 200), (200, 200),
                  (-250, 150), (-200, 150), (-100, 150), (0, 150),
                  (-200, 100), (0, 100), (50, 100), (100, 100), (200, 100), (250, 100),
                  (-100, 50), (0, 50), (50, 50), (200, 50),
                  (-200, 0), (-150, 0), (-100, 0), (0, 0), (50, 0), (150, 0), (200, 0),
                  (-250, -50), (-200, -50), (200, -50),
                  (-100, -100), (-50, -100), (0, -100), (100, -100), (200, -100),
                  (-200, -150), (-150, -150), (-100, -150), (100, -150),
                  (-100, -200), (-50, -200), (0, -200), (50, -200), (100, -200), (150, -200), (200, -200),
                  (-250, -250), (-200, -250), (-150, -250), (-100, -250)
                  )

# Pacman의 위치와 gem 위치입니다
position = [-250, 250]
treasure = [250, -250]

# 바운더리와 장애물을 체크해주는 함수입니다
def checkBoudary(posX, posY):
    tempTuple = (posX, posY)
    if 275 > posX > -275 and 275 > posY > -275:
        for i in block_position:
            if i != tempTuple:
                print("noblock")
            else:
                return False
    else:
        print("out of bounds")
        return False

def function():
    global position
    global treasure
    while True:
        randomNum = randrange(4)
        # go up
        print(position)
        if randomNum == 3:
            position[1] = position[1] + 50
            if checkBoudary(position[0], position[1]) is False:
                position[1] = position[1] - 50
            else:
                shape(image["up"])
                goto(position[0], position[1])
        # go right
        elif randomNum == 2:
            position[0] = position[0] + 50
            if checkBoudary(position[0], position[1]) is False:
                position[0] = position[0] - 50
            else:
                shape(image["right"])
                goto(position[0], position[1])
        # go down
        elif randomNum == 1:
            position[1] = position[1] - 50
            if checkBoudary(position[0], position[1]) is False:
                position[1] = position[1] + 50
            else:
                shape(image["down"])
                goto(position[0], position[1])
        # go left
        else:
            position[0] = position[0] - 50
            if checkBoudary(position[0], position[1]) is False:
                position[0] = position[0] + 50
            else:
                goto(position[0], position[1])
                shape(image["left"])
        if position == treasure:
            break


# 여기서 함수들을 실행시킵니다
drawMap()
setUpPacman()
function()
exitonclick()
