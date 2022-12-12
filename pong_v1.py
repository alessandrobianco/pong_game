# PONG GAME
# ==============
# import del modulo turtle, che userò per creare la grafica del gioco
import turtle
# setup iniziale della finestra di gioco (win)
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # provare a rimuoverlo a gioco finito per vedere la differenza

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# score
score_a = 0
score_b = 0

# setup racchette e pallina
rac_a = turtle.Turtle()
rac_a.speed(0)
rac_a.shape("square")
rac_a.color("white")
rac_a.shapesize(stretch_wid=5, stretch_len=1)
rac_a.penup()
rac_a.goto(-350, 0)

rac_b = turtle.Turtle()
rac_b.speed(0)
rac_b.shape("square")
rac_b.color("white")
rac_b.shapesize(stretch_wid=5, stretch_len=1)
rac_b.penup()
rac_b.goto(350, 0)

pallina = turtle.Turtle()
pallina.speed(0)
pallina.shape("square")
pallina.color("white")
pallina.penup()
pallina.goto(0, 0)
pallina.dx = 5  #  muove sempre di 2px
pallina.dy = 5

# funzioni


def rac_a_up():
    y = rac_a.ycor()
    y += 20
    rac_a.sety(y)


def rac_a_down():
    y = rac_a.ycor()
    y -= 20
    rac_a.sety(y)


def rac_b_up():
    y = rac_b.ycor()
    y += 20
    rac_b.sety(y)


def rac_b_down():
    y = rac_b.ycor()
    y -= 20
    rac_b.sety(y)


# settaggio tasti
win.listen()
win.onkeypress(rac_a_up, "w")
win.onkeypress(rac_a_down, "s")
win.onkeypress(rac_b_up, "Up")
win.onkeypress(rac_b_down, "Down")

# main game loop
while True:
    win.update()

    # movimento pallina
    pallina.setx(pallina.xcor() + pallina.dx)
    pallina.sety(pallina.ycor() + pallina.dy)

    # controllo bordi
    if pallina.ycor() > 290:
        pallina.sety(290)
        pallina.dy *= -1

    if pallina.ycor() < -290:
        pallina.sety(-290)
        pallina.dy *= -1

    if pallina.xcor() > 390:
        pallina.goto(0, 0)
        pallina.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center",
                  font=("Courier", 24, "normal"))

    if pallina.xcor() < -390:
        pallina.goto(0, 0)
        pallina.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center",
                  font=("Courier", 24, "normal"))

    # impatto racchetta pallina
    if (pallina.xcor() > 340 and pallina.xcor() < 350) and (pallina.ycor() < rac_b.ycor() + 40 and pallina.ycor() > rac_b.ycor() - 40):
        pallina.setx(340)
        pallina.dx *= -1

    if (pallina.xcor() < -340 and pallina.xcor() > -350) and (pallina.ycor() < rac_a.ycor() + 40 and pallina.ycor() > rac_a.ycor() - 40):
        pallina.setx(-340)
        pallina.dx *= -1
