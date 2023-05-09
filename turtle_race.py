from turtle import *
from random import *


class Players(Turtle):
    def __init__(self, color, speed, step, y):
        super().__init__()
        self.ht()
        self.color(color)
        self.shape('turtle')
        self.speed(speed)
        self.step = step
        self.penup()
        self.goto(-100, y)
        self.st()

    def move(self):
        self.fd(self.step)

    def check(self):
        if self.xcor() >= 190:
            return True
        return False


def picture(t):
    t.st()
    t.goto(0, 0)
    t.speed(8)
    t.ht()
    t.goto(0, 100)
    t.st()
    for _ in range(30):
        t.stamp()
        t.fd(30)
        t.right(360/30)


def stars(x, y):
    speed(10)
    penup()
    color('yellow')
    goto(x, y)
    pendown()
    for _ in range(5):
        fd(30)
        left(144)


def win(t):
    t.speed(3)
    t.goto(-30, 15)
    t.write('Win!!!', font=('Verdana', 30, 'normal'))
    t.goto(15, -25)


bgcolor('lavender')
color('brown')
pensize(4)
speed(10)
ht()
penup()
goto(-100, 100)
pendown()
right(90)
fd(200)
penup()
goto(200, 100)
pendown()
fd(200)

t1 = Players('light coral', randrange(1, 5), randrange(3, 15), 75)
t2 = Players('light blue', randrange(1, 5), randrange(3, 15), 25)
t3 = Players('pale violet red', randrange(1, 5), randrange(3, 15), -25)
t4 = Players('purple', randrange(1, 5), randrange(3, 15), -75)

players = (t1, t2, t3, t4)

while not t1.check() and not t2.check() and not t3.check() and not t4.check():
    for player in players:
        player.move()

for player in players:
    player.ht()
clear()

winner_xcor = max(t1.xcor(), t2.xcor(), t3.xcor(), t4.xcor())
if t1.xcor() == winner_xcor:
    picture(t1)
    win(t1)
elif t2.xcor() == winner_xcor:
    picture(t2)
    win(t2)
elif t3.xcor() == winner_xcor:
    picture(t3)
    win(t3)
else:
    picture(t4)
    win(t4)

stars(-50, -70)
stars(10, -70)
stars(70, -70)

done()
