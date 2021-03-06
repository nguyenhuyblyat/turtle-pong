#!/usr/env/python

import turtle
# very fucky library ^^^^^^
i = 0  # counter
paddleSpeed = 60

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
paddleA.color("white")
paddleA.pu()
paddleA.goto(-350, 0)
# player 1 ^^^^^^^^

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.pu()
paddleB.goto(350, 0)
# player 2 ^^^^^^^^^^

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.pu()
# ball .-. ^^^^^^^^^^^^

playerA = 0 # player 1's score
playerB = 0 # player 2's score
# score system ^^^^^^^^^^

def padAup():
	y = paddleA.ycor()
	y += paddleSpeed
	paddleA.sety(y)

def padBup():
	y = paddleB.ycor()
	y += paddleSpeed
	paddleB.sety(y)

def padAdown():
	y = paddleA.ycor()
	y -= paddleSpeed
	paddleA.sety(y)

def padBdown():
	y = paddleB.ycor()
	y -= paddleSpeed
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

    if paddleA.ycor() > 240:
    	paddleA.sety(240)
    elif paddleA.ycor() < -240:
    	paddleA.sety(-240)
    if paddleB.ycor() > 240:
    	paddleB.sety(240)
    elif paddleB.ycor() < -240:
    	paddleB.sety(-240)
    # anti-voiding the paddles, or it will break the game lol
    
# da loop runs 4ever ^^^^^^
