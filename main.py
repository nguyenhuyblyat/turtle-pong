#!/usr/env/python

import turtle
from random import *
from time import *
# importing libraries ^^^^^^
winningPoint = 100
paddleDistancePerClick = 80
ballSpeed = 2.5
# important variables xDDDDD ^^^^^^^^^^

def moveGap(tur):
    tur.pu()
    tur.fd(2)
    tur.pd()
# gap between each segment ^^^^^^^^^^^

def drawLine(draw, tur):
    moveGap(tur)
    tur.pd() if draw else tur.pu()
    tur.fd(20)
    moveGap(tur)
    tur.rt(90)
# function to draw a single segment ^^^^^^^^^^^^^^^

def drawDigit(digits, tur):  # Drawing seven section digital tube according to the number
    for digit in str(digits):
        digit = int(digit)
        drawLine(True, tur) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False, tur)
        drawLine(True, tur) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False, tur)
        drawLine(True, tur) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False, tur)
        drawLine(True, tur) if digit in [0, 2, 6, 8] else drawLine(False, tur)
        tur.left(90)
        drawLine(True, tur) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False, tur)
        drawLine(True, tur) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False, tur)
        drawLine(True, tur) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False, tur)
        tur.left(180)
        tur.pu()  # Position for drawing subsequent numbers
        tur.fd(20)  # Position for drawing subsequent numbers
# function to draw the digit in seven segment ^^^^^^^^^^

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
window.setup(width=1.0, height=1.0)
canvas = window.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
window.tracer(0)

borderHighlight = turtle.Turtle()
borderHighlight.speed(0)
borderHighlight.color("white")
borderHighlight.hideturtle()
borderHighlight.pensize(15)
borderHighlight.pu()
borderHighlight.goto(-400, 300)
borderHighlight.pd()
for i in range(2):
    borderHighlight.forward(800)
    borderHighlight.right(90)
    borderHighlight.forward(600)
    borderHighlight.right(90)
# fullscreen window and borders ^^^^^^^^^^^

net = turtle.Turtle()
net.speed(0)
net.color("white")
net.pu()
net.hideturtle()
net.goto(0, 300)
net.right(90)
drawDottedLine(net, 5, 15, 41)
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
ballDirectionX = ballSpeed
ballDirectionY = -ballSpeed
# ball .-. ^^^^^^^^^^^^

playerA = 0 # player 1's score
playerB = 0 # player 2's score
scoreboard1 = turtle.Turtle()
scoreboard1.pensize(10)
scoreboard1.speed(0)
scoreboard1.color("white")
scoreboard1.pu()
scoreboard1.hideturtle()
scoreboard1.goto(-250, 240)
drawDigit(playerA, scoreboard1)
scoreboard1.goto(-250, 240)

scoreboard2 = turtle.Turtle()
scoreboard2.pensize(10)
scoreboard2.speed(0)
scoreboard2.color("white")
scoreboard2.pu()
scoreboard2.hideturtle()
scoreboard2.goto(250, 240)
drawDigit(playerB, scoreboard2)
scoreboard2.goto(250, 240)

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
    if playerA == winningPoint:
        ballDirectionX = 0
        ballDirectionY = 0
        ball.setx(0)
        ball.sety(0)
        scoreboard1.clear()
        scoreboard1.write("Winner!", align="center", font=("", 24, "normal"))
        sleep(2.5)
        window.bye()
    elif playerB == winningPoint:
        ballDirectionX = 0
        ballDirectionY = 0
        ball.setx(0)
        ball.sety(0)
        scoreboard2.clear()
        scoreboard2.write("Winner!", align="center", font=("", 24, "normal"))
        sleep(2.5)
        window.bye()
    # Checks if either player has won, announce the winner, wait for 2.5 seconds and halt the program

    ## print("Ball X: " + str(ball.xcor()) + " Ball Y: " + str(ball.ycor()) + " Dx: " + str(ballDirectionX) + " Dy: " + str(ballDirectionY)) 
    # uncomment this for debugging ^^^^^^^^^

    ball.sety(ball.ycor() + ballDirectionY)
    ball.setx(ball.xcor() + ballDirectionX)
    # moving ball ^^^^^^^^^^

    if ball.ycor() > 300:
    	ball.sety(300)
    	ballDirectionY *= -1
    if ball.ycor() < -300:
    	ball.sety(-300)
    	ballDirectionY *= -1
    if ball.xcor() > 400:
        ball.setx(400)
        ballDirectionX *= -1
        playerA += 1
        scoreboard1.clear()
        drawDigit(playerA, scoreboard1)
        scoreboard1.goto(-250, 240)
        ball.setx(0)
        ball.sety(randint(-200, 200))
    if ball.xcor() < -400:
        ball.setx(-400)
        ballDirectionX *= -1
        playerB += 1
        scoreboard2.clear()
        drawDigit(playerB, scoreboard2)
        scoreboard2.goto(250, 240)
        ball.setx(0)
        ball.sety(randint(200, 200))
    # anti-voiding ball, border collisions and score increments ^^^^^^^^^^

    if paddleA.ycor() > 250:
    	paddleA.sety(250)
    elif paddleA.ycor() < -256:
    	paddleA.sety(-256)
    if paddleB.ycor() > 250:
    	paddleB.sety(250)
    elif paddleB.ycor() < -256:
    	paddleB.sety(-256)
    # anti-voiding paddles ^^^^^^^^

    if (ball.xcor() < 355 and ball.xcor() > 345 ) and (ball.ycor() < paddleB.ycor() + 55 and ball.ycor() > paddleB.ycor() - 55):
    	ball.setx(345)
    	ballDirectionX *= -1
    if (ball.xcor() > -355 and ball.xcor() < -345 ) and (ball.ycor() < paddleA.ycor() + 55 and ball.ycor() > paddleA.ycor() - 55):
    	ball.setx(-345)
    	ballDirectionX *= -1
    # paddles collisions ^^^^^^^^^^^
# da loop runs 4ever ^^^^^^