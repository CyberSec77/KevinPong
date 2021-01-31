# A small game of pong I made over a day

import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("KevPong by Kevin Babiuk")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scoring System
score_a = 0
score_b = 0

win = turtle.Screen()

win.bgpic('imageNew.gif')


# Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Cool Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Kid 1: 0 Kid 2: 0", align="center", font=("Comic Sans MS", 24, "italic"))

# Move Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -10
    paddle_b.sety(y)

# Controls
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Start 
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border find
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay Border.wav&")
        os.system("aflay Border.wav&")
        winsound.PlaySound("Border.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay Border.wav&")
        os.system("aflay Border.wav&")
        winsound.PlaySound("Border.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Kid 1: {} Kid 2: {}".format(score_a,score_b), align="center", font=("Comic Sans MS", 24, "italic"))
        os.system("aplay Yay.wav&")
        os.system("aflay Yay.wav&")
        winsound.PlaySound("Yay.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Kid 1: {} Kid 2: {}".format(score_a,score_b), align="center", font=("Comic Sans MS", 24, "italic"))
        os.system("aplay Yay.wav&")
        os.system("aflay Yay.wav&")
        winsound.PlaySound("Yay.wav", winsound.SND_ASYNC)

    # Paddle and ball colliding
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay Bounce.wav&")
        os.system("aflay Bounce.wav&")
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay Bounce.wav&")
        os.system("aflay Bounce.wav&")
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)