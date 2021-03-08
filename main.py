#!/usr/env/python

import turtle
from random import *
from time import *
# importing libraries ^^^^^^

paddleDistancePerClick = 80
ballSpeed = 1.5
# important variables xDDDDD ^^^^^^^^^^

def drawDottedLine(tur, sizeOfSide, spaceBetweenDots, numberOfDots):
    for i in range(numberOfDots):
        tur.pd()
        tur.begin_fill()
        for x in range(4):
            tur.forward(sizeOfSide)
            tur.left(90)
        tur.end_fill()
        tur.pu()
        tur.forward(spaceBetweenDots)
# function to draw dotted line ^^^^^^^

window = turtle.Screen()
window.title("@nguyenhuyblyat | Pong!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# 800x600 window ^^^^^^^^^^^

net = turtle.Turtle()
net.speed(0)
net.color("white")
net.pu()
net.hideturtle()
net.goto(0, 295)
net.right(90)
drawDottedLine(net, 20, 35, 20)
# ^^^^^^^^^ this is the function to draw the net, it's positional arguments are: the turtle to draw with (net), the size of each side (20), the distance between each dot (35), the number of dots (20)
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
# scoreboard ^^^^^^^^^^

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
    if playerA == 5:
        ballDx = 0
        ballDy = 0
        ball.setx(0)
        ball.sety(0)
        scoreboard.clear()
        scoreboard.write("Winner!                   {}".format(playerB), align="center", font=("Courier", 24, "normal"))
        sleep(2.5)
        window.bye()
    elif playerB == 5:
        ballDx = 0
        ballDy = 0
        ball.setx(0)
        ball.sety(0)
        scoreboard.clear()
        scoreboard.write("{}                   Winner!".format(playerA), align="center", font=("Courier", 24, "normal"))
        sleep(2.5)
        window.bye()
    # Checks if either player has won, announce the winner, wait for 2.5 seconds and halt the program

    print("Ball X: " + str(ball.xcor()) + " Ball Y: " + str(ball.ycor()) + " Dx: " + str(ballDx) + " Dy: " + str(ballDy)) 
    # uncomment this for debugging ^^^^^^^^^

    ball.sety(ball.ycor() + ballDy)
    ball.setx(ball.xcor() + ballDx)
    # moving ball ^^^^^^^^^^

    if ball.ycor() > 300:
    	ball.sety(300)
    	ballDy *= -1
    if ball.ycor() < -300:
    	ball.sety(-300)
    	ballDy *= -1
    if ball.xcor() > 400:
    	ball.setx(400)
    	ballDx *= -1
    	playerA += 1
    	scoreboard.clear()
    	scoreboard.write("{}                     {}".format(playerA, playerB), align="center", font=("Courier", 24, "normal"))
    	ball.setx(0)
    	ball.sety(0)
    if ball.xcor() < -400:
    	ball.setx(-400)
    	ballDx *= -1
    	playerB += 1
    	scoreboard.clear()
    	scoreboard.write("{}                     {}".format(playerA, playerB), align="center", font=("Courier", 24, "normal"))
    	ball.setx(0)
    	ball.sety(0)
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
 