import turtle

rahul = turtle.Screen()
rahul.bgcolor("black")
rahul_jerthi = turtle.Turtle()
rahul_jerthi.width(7)
colors = ["#f5ac2f", "#279cf5", "#d820f5", "#a2f52f", "#f527c1"]


def draw_rj(i, x, y):
    rahul_jerthi.pencolor("linen")
    rahul_jerthi.color(colors[i % 7])
    rahul_jerthi.lt(70)
    rahul_jerthi.penup()
    rahul_jerthi.goto(x, y)
    rahul_jerthi.pendown()
    rahul_jerthi.circle(22)
    rahul_jerthi.end_fill()


def ballon(x, y):
    rahul_jerthi.pensize(4)
    for i in range(5):
        draw_rj(i, x, y)




def cake(x, y):
    rahul_jerthi.fd(x)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(y)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(x)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(y)


def move(x, y):
    rahul_jerthi.up()
    rahul_jerthi.setposition(0, 0)
    rahul_jerthi.setheading(90)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(x)
    rahul_jerthi.lt(90)
    rahul_jerthi.fd(y)
    rahul_jerthi.pendown()


def mov(x, y):
    rahul_jerthi.up()
    rahul_jerthi.setposition(0, 0)
    rahul_jerthi.setheading(90)
    rahul_jerthi.lt(90)
    rahul_jerthi.fd(x)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(y)
    rahul_jerthi.pendown()


def A(size):
    rahul_jerthi.rt(19)
    rahul_jerthi.forward(size)
    rahul_jerthi.rt(141)
    rahul_jerthi.fd(size)
    rahul_jerthi.backward(size / 2)
    rahul_jerthi.rt(105)
    rahul_jerthi.fd(int(size / 3))


def B(size):
    rahul_jerthi.forward(size)
    rahul_jerthi.rt(90)
    for i in range(18):
        rahul_jerthi.rt(9)
        rahul_jerthi.fd(size // 20)
    for i in range(18):
        rahul_jerthi.rt(size // 5)
        rahul_jerthi.backward(size // 20)


def D(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(size // 10)
    for i in range(13):
        rahul_jerthi.rt(13)
        rahul_jerthi.fd(size // 8)


def E(size):
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(int(size / 3))
    rahul_jerthi.back(int(size / 3))
    rahul_jerthi.left(90)
    rahul_jerthi.fd(size / 2)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(int(size / 3))
    rahul_jerthi.back(int(size / 3))
    rahul_jerthi.lt(90)
    rahul_jerthi.fd(size / 2)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(int(size / 3))


def H(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.backward(size // 2)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(size // 2)
    rahul_jerthi.lt(90)
    rahul_jerthi.fd(size // 2)
    rahul_jerthi.backward(size)


def I(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.rt(90)
    rahul_jerthi.circle(size // 8)

def L(size):
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(int(size / 2))
    rahul_jerthi.back(int(size / 2))
    rahul_jerthi.lt(90)
    rahul_jerthi.fd(size)

def N(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.rt(150)
    rahul_jerthi.fd(size + int(size / 6))
    rahul_jerthi.lt(150)
    rahul_jerthi.fd(size)


def P(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(size // 8)
    for i in range(8):
        rahul_jerthi.rt(20)
        rahul_jerthi.fd(size // 9)

def R():
    rahul_jerthi.fd(60)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(7)
    for i in range(15):
        rahul_jerthi.rt(12)
        rahul_jerthi.fd(3)
    rahul_jerthi.lt(120)
    rahul_jerthi.fd(40)


def S(size):
    rahul_jerthi.rt(90)
    for i in range(0, 5):
        if i < 3:
            rahul_jerthi.fd(size / 2)
            rahul_jerthi.lt(90)
            if i == 2:
                rahul_jerthi.rt(90)
        else:
            rahul_jerthi.right(90)
            rahul_jerthi.fd(size / 2)


def T(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(size // 2)
    rahul_jerthi.backward(size // 2)


def Y(size):
    rahul_jerthi.fd(size)
    rahul_jerthi.left(60)
    rahul_jerthi.fd(size // 2)
    rahul_jerthi.backward(size // 2)
    rahul_jerthi.rt(90)
    rahul_jerthi.fd(size // 1.5)

rahul_jerthi.speed(19)


mov(120, 30)
rahul_jerthi.color("#f7b543")
# rahul_jerthi.color(colors[8 % 5])
rahul_jerthi.begin_fill()
cake(40, 180)
rahul_jerthi.end_fill()
mov(110, 75)
rahul_jerthi.color("#d152f7")
rahul_jerthi.begin_fill()
cake(40, 160)
rahul_jerthi.end_fill()
mov(100, 120)
rahul_jerthi.color("#f54eb8")
rahul_jerthi.begin_fill()
cake(40, 140)
rahul_jerthi.end_fill()
mov(30, 170)
rahul_jerthi.width(11)
rahul_jerthi.pencolor("red")
rahul_jerthi.circle(7)
move(180, 307)
mov(0, 0)
ballon(-490, 200)
ballon(490, 200)
ballon(183, -150)
ballon(-133, -150)

rahul_jerthi.speed(7)
rahul_jerthi.width(9)
rahul_jerthi.pencolor("#319df5")


mov(260, 205)
S(size=70)

rahul_jerthi.width(11)

mov(200, 205)
N(70)


mov(135, 205)
E(size=70)


mov(90, 205)
H(size=70)


mov(40, 205)
A(size=70)


rahul_jerthi.pencolor("#95ed28")
style = ('Arial', 50, 'italic')


rahul_jerthi.pencolor("cyan")
rahul_jerthi.width(13)


mov(260, -80)
H(100)


rahul_jerthi.width(7)
mov(190, -80)


A(65)
mov(135, -80)


P(60)
mov(100, -80)


P(60)
mov(52, -80)


Y(60)
mov(28, -80)


B(60)
move(12, -80)


I(60)
move(36, -80)


R()
move(80, -80)


T(100)
move(102, -80)


H(60)
move(150, -80)


rahul_jerthi.pencolor('hotpink')
D(200)


move(160, -80)
A(60)


move(220, -80)
Y(60)




rahul.exitonclick()