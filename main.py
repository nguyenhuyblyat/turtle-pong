#!/usr/env/python

import turtle
from random import *
# importing libraries ^^^^^^

paddleDistancePerClick = 80
ballSpeed = 2
# important variables xDDDDD ^^^^^^^^^^

window = turtle.Screen()
window.title("@nguyenhuyblyat | Pong!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# window ^^^^^^^^^^^

net = turtle.Turtle()
net.speed(0)
net.shape("square")
net.shapesize(stretch_wid=100, stretch_len=0.5)
net.color("White")
net.pu()
# net ^^^^^^^^^^^^^^

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.pu()
paddleA.goto(-350, 0)
# paddle 1 ^^^^^^^^

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.pu()
paddleB.goto(350, 0)
# paddle 2 ^^^^^^^^^^

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
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

def quitPong():
	window.bye()
# quit game :( ^^^^^^^^^

window.listen()
window.onkeypress(padAup, "a")
window.onkeypress(padAdown, "z")
window.onkeypress(padBup, "k")
window.onkeypress(padBdown, "m")
window.onkeypress(quitPong, "y")
# keyboard bindings and listening ^^^^^^^^^^^^

while True:

    window.update()
    print(ball.xcor())
    ball.sety(ball.ycor() + ballDy)
    ball.setx(ball.xcor() + ballDx)
    # moving ball ^^^^^^^^^^

    if ball.ycor() > 300:
    	ball.sety(280)
    	ballDy *= -1
    if ball.ycor() < -300:
    	ball.sety(-280)
    	ballDy *= -1
    if ball.xcor() > 400:
    	ball.setx(400)
    	ballDx *= -1
    	playerA += 1
    	scoreboard.clear()
    	scoreboard.write("{}                     {}".format(playerA, playerB), align="center", font=("Courier", 24, "normal"))
    	ball.setx(0)
    	ball.sety(randint(-100, 100))
    if ball.xcor() < -400:
    	ball.setx(-400)
    	ballDx *= -1
    	playerB += 1
    	scoreboard.clear()
    	scoreboard.write("{}                     {}".format(playerA, playerB), align="center", font=("Courier", 24, "normal"))
    	ball.setx(0)
    	ball.sety(randint(-100, 100))
    # anti-voiding ball, border collisions and score increments ^^^^^^^^^^

    if paddleA.ycor() > 260:
    	paddleA.sety(260)
    elif paddleA.ycor() < -260:
    	paddleA.sety(-260)
    if paddleB.ycor() > 260:
    	paddleB.sety(260)
    elif paddleB.ycor() < -260:
    	paddleB.sety(-260)
    # anti-voiding paddles ^^^^^^^^

    if (ball.xcor() < 355 and ball.xcor() > 345 ) and (ball.ycor() < paddleB.ycor() + 55 and ball.ycor() > paddleB.ycor() - 55):
    	ball.setx(345)
    	ballDx *= -1
    if (ball.xcor() > -355 and ball.xcor() < -345 ) and (ball.ycor() < paddleA.ycor() + 55 and ball.ycor() > paddleA.ycor() - 55):
    	ball.setx(-345)
    	ballDx *= -1
    # paddles collisions ^^^^^^^^^^^
# da loop runs 4ever ^^^^^^
 