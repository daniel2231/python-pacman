# 파이썬 팩맨 개발문서

- 코드 보기

    ```python
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
    ```

# 코드 실행 설명

### 1. 미로 좌표 찾기

미로를 x, y 좌표로 표현해주면 아래와 같이 나옵니다.

- 가로: 550px
- 세로: 550px
- 스크린 크기: 600px
- 시작 좌표: (250, 250)
- gem의 좌표: (250, -250)

### 2. 테두리 세팅

```python
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
```

1. 스크린 크기와 미로를 세팅해줍니다. 미로의 좌표대로 테두리를 그려줍니다.

### 3. 미로 그리기

```python
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
```

1. 미로에 있는 장애물들의 위치를 배열과 숫자로 표현합니다. 쉽게 말해 표에 장애물의 위치를 찍은것과 동일합니다.
    - 0 = 장애물 없음
    - 1 = 장애물 있음
    - 3 = 다음 행으로 이동
2. 장애물을 그리기 위한 함수를 만듭니다. 
3. 미로를 그려주기위한 함수를 만듭니다.
    - for loop을 이용해줍니다.
    - 현재 배열안에 배열이 있고, 그 안에 숫자가 있습니다.
    - for i in obstacles는 "배열 안에 각 배열마다"를 뜻하고
    - for i in j는 "그 배열 안에 있는 각 숫자마다"를 뜻합니다.
    - 그 안에는 if문을 돌려서 0일땐 터틀을 앞으로,
    - 3일때는 다음 행으로,
    - 나머지인 1 일땐 장애물을 그려주게 합니다.

### 4. 팩맨과 장애물 좌표 세팅

```python
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

```

1. 팩맨을 세팅해줍니다.
    - 두번째 터틀을 생성해 gem의 역할을 하게 합니다
    - 팩맨을 첫 시작점으로 옮겨줍니다.
    - 팩맨이 가는 위치에 따라 이미지가 바뀌도록 팩맨의 다양한 사진들을 shape로 선언해줍니다. (선언한 이미지만 터틀의 이미지로 쓸 수 있습니다)

2. 장애물의 위치를 좌표로 나타내줍니다.
    1. 장애물의 위치는 x,y 좌표로, 값이 바뀔 수 없게 tuple을 이용하여 설정해줍니다.

### 5. 팩맨 실행

```python
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
				# 팩맨의 좌표와 gem의 좌표가 같을때 반복문을 빠져나옵니다
        if position == treasure:
            break
```

1. 팩맨의 위치와 gem의 위치를 저장하는 변수를 만듭니다.
2. 팩맨이 미로밖을 나가지 않고, 장애물을 통과하지 않도록 체크해주는 함수를 만듭니다. checkBoundary라고 하겠습니다.
    - 매개변수로 posX, posY를 설정해줍니다.

    매개변수란?
    매개변수는 함수에 전달되는 값을 받아주기 위한 변수입니다.
    예를 들어 두 숫자를 더해주는 함수를 만들고 싶으면:
    def addSum(x,y):
         print(x + y)

    이렇게 만들고, 더해줄 숫자를 x와 y에 써주면:
    addSum(1,2)
    >>> 3
    3이 나옵니다.

    쉽게, 함수에 값을 전달하는 역할을 합니다.

    - tempTuple 안에 전달받은 x와 y 좌표를 튜플형태로 저장합니다. 튜플로 저장한 이유는 장애물의 좌표가 튜플로 저장되어 있는데, 이 둘을 비교하기 위해선 자료형이 같아야 하기 때문입니다. 한마디로, 튜플은 튜플이랑만 비교가 가능합니다.
    - 팩맨이 미로를 나가면 안됨으로 x와 y 값이 275보다는 작고, -275보다는 클때 움직일 수 있도록 함수를 만듭니다.
    - 팩맨이 장애물을 통과하지 못하도록 장애물 좌표가 저장되어 있는 변수에 for 문을 돌려 만약 팩맨의 다음 이동 좌표가 장애물 좌표와 같다면 false를 출력하도록 만듭니다.
    - 만약 장애물이 없다면 아무 방해없이 for 문을 벗어납니다. 다만 확인용으로 `print("noblock")`을 써줍니다.

3. 팩맨이 실행되는 코드를 작성해줍니다
    - Global을 선언한 이유는 함수 밖에 있는 변수에도 접근이 가능하도록 해주기 위해서입니다.
    - While True를 써서 무한 반복을 하되, 팩맨의 좌표와 gem의 좌표가 같으면 반복문에서 빠져 나올 수 있도록 `break`를 써줍니다.
    - randrange(4)를 사용해 0 ~ 3까지 숫자가 나오도록 합니다.
    - 그 후론 각 숫자가 나올때 실행되는 코드를 짜줍니다. 형태는 다 같음으로 3일때 실행되는 코드를 예를 들어보겠습니다.
        - position[1]에 50을 더해줍니다. position[1]은 position 배열의 두번째 값을 뜻합니다. 배열에 순서를 인덱스라고 하는데, 인덱스는 항상 0부터 시작합니다. 배열에 두번째 값의 인덱스는 고로 1입니다.
            - 여기서 코드를 더 간결하게 하기 위해 `position[1] += 50` 이렇게 써도 됩니다.
        - 위에 만들어준 checkBoundary를 돌려줍니다. 매개변수로 x와 y값을 전달합니다.
            - 전달되 x와 y값이 미로를 벗어나지 않고, 장애물을 통과하지 않는다면 True가 나옵니다.
            - 그렇지 않은 경우 False가 나옵니다.
        - True일때, 해당 좌표로 이동합니다.
        - False일때, position[1]에서 50을 빼줍니다.

### 5. 만들어준 함수들을 순서에 맞게 실행시킵니다.

```python
# 여기서 함수들을 실행시킵니다
drawMap()
setUpPacman()
function()
exitonclick()
```