#!/usr/env/python

import turtle
# importing the only library ^^^^^^

paddleDistancePerClick = 60
ballSpeed = 1.2
# important variables xDDDDD ^^^^^^^^^^

window = turtle.Screen()
window.title("@nguyenhuyblyat | Pong!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

net = turtle.Turtle()
net.speed(0)
net.shape("square")
net.shapesize(stretch_wid=100, stretch_len=0.5)
net.color("White")
net.pu()

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("red")
paddleA.pu()
paddleA.goto(-350, 0)
# paddle 1 ^^^^^^^^

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("blue")
paddleB.pu()
paddleB.goto(350, 0)
# paddle 2 ^^^^^^^^^^

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.pu()
ballDx = ballSpeed
ballDy = -ballSpeed
# ball .-. ^^^^^^^^^^^^

playerA = 0 # player 1's score
playerB = 0 # player 2's score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.pu()
scoreboard.hideturtle()
scoreboard.goto(0, 255)
scoreboard.write("0                     0", align="center", font=("Courier", 24, "normal"))

# score system ^^^^^^^^^^

def padAup():
	y = paddleA.ycor()
	y += paddleDistancePerClick
	paddleA.sety(y)

def padBup():
	y = paddleB.ycor()
	y += paddleDistancePerClick
	paddleB.sety(y)

def padAdown():
	y = paddleA.ycor()
	y -= paddleDistancePerClick
	paddleA.sety(y)

def padBdown():
	y = paddleB.ycor()
	y -= paddleDistancePerClick
	paddleB.sety(y)
# functions to move the paddles ^^^^^^^^^^^

window.listen()
window.onkeypress(padAup, "a")
window.onkeypress(padAdown, "z")
window.onkeypress(padBup, "k")
window.onkeypress(padBdown, "m")
# keyboard bindings and listening ^^^^^^^^^^^^

while True:
    window.update()
    print(ball.xcor())
    ball.sety(ball.ycor() + ballDy)
    ball.setx(ball.xcor() + ballDx)
    # moving ball ^^^^^^^^^^

    if ball.ycor() > 280:
    	ball.sety(280)
    	ballDy *= -1
    if ball.ycor() < -280:
    	ball.sety(-280)
    	ballDy *= -1
    if ball.xcor() > 400:
    	ball.setx(400)
    	ballDx *= -1
    	playerA += 1
    	scoreboard.clear()
    	scoreboard.write("{}                     {}".format(playerA, playerB), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -400:
    	ball.setx(-400)
    	ballDx *= -1
    	playerB += 1
    	scoreboard.clear()
    	scoreboard.write("{}                     {}".format(playerA, playerB), align="center", font=("Courier", 24, "normal"))
    # anti-voiding ball and collisions ^^^^^^^^^^

    if paddleA.ycor() > 260:
    	paddleA.sety(260)
    elif paddleA.ycor() < -260:
    	paddleA.sety(-260)
    if paddleB.ycor() > 260:
    	paddleB.sety(260)
    elif paddleB.ycor() < -260:
    	paddleB.sety(-260)
    # anti-voiding paddles ^^^^^^^^

    if (ball.xcor() < 355 and ball.xcor() > 345 ) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
    	ball.setx(345)
    	ballDx *= -1
    if (ball.xcor() > -355 and ball.xcor() < -345 ) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
    	ball.setx(-345)
    	ballDx *= -1
    # paddles collisions ^^^^^^^^^^^
# da loop runs 4ever ^^^^^^
 