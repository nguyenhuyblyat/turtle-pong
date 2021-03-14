The famous "Pong!" game, recreated in Python 3.9.2 with built-in Turtle library.	

Note: This program is released under GNU General Public License version 3, all forks of this program are allowed as long as they are open-source. Full version of the license can be found in the repository under the name `LICENSE`.

## Prerequisites
	- Python 3.x (https://python.org/)
	- Turtle (built-in within Python)
	- random (built-in within Python)
	- time (built-in within Python)

## Running
	- `python3 main.py`
	- `python main.py` if the above doesn't work (edge cases)

## Controls
	- Player 1 (left): A for up, Z for down
	- Player 2 (right): K for up, M for down
	- Quit: Y

## Magic Hax
	- Step 1: Create an fullscreen window with Turtle, with a black background and a border around the game.
	- Step 2: Define a function to draw a dotted line:
		+ In the function `drawDottedLine` in my code, it requires 4 arguments:
			_ The turtle to draw the dotted line
			_ The size of each dot's side. (This is a square dot)
			_ The space between each dot
			_ The number of dots to draw
		+ Step 2.1: Turtle's pendown (to begin drawing) and starts filling each closed shape with the turtle's color
		+ Step 2.2: Make the turtle goes forward (which is downward) and turns left or right 90 degrees for 4 times.
		+ Step 2.3: After it finished drawing the square, stop filling and turtle's penup so it won't draw anymore
		+ Step 2.4: Make the turtle goes forward the same distance as the space between each dot
		+ Step 2.5 Repeat the process from 2.1 to 2.4 as many times as you want, ideally enough to fit the whole screen.
	- Step 3: Create a net turtle and call the function `drawDottedLine` with the criterion that I've just mentioned earlier.
	- Step 4: Create the paddles and the ball to hit with.
		+ Move the paddles to near the left and right border of the screen
		+ The ball stays at [0, 0]
	- Step 5: Define functions to move the paddles, and to quit the game
		+ Paddle 1 up, down
		+ Paddle 2 up, down
		+ Quiting the game
	- Step 6: Create a scoring system:
		+ Step 6.1: Initialize player 1's and player 2's score (0  -  0)
		+ Step 6.2: Create a turtle Object and draw seven-segments number (Explanation below)
		+ Step 6.3: Display the scoreboard on top of the screen
    - Step 7: Make the ball move:
            + Step 7.1: Create 2 variables DirectionX, DirectionY.
            + Step 7.2: Add DirectionX with ball's xcor(), DirectionY with ball's ycor().
            Explanation: Imagine the whole window is a graph, and the ball is at [0, 0]. Every time the loop runs, it will add a specific value to ball's x and y. Let's assume the Dx = 1 and Dy = 1. Every time the loop runs, the coordinates of the ball is constantly rising from [0, 0] to [1, 1] and [2, 2] and so on... The ball is corresponding with the gradient: y = x
	- Step 8: Borders collisions:
		+ Upper and lower borders will bounce the ball off
			_ If ball's ycor() is larger than 300, sety() to 300 and change bearing by a specific degree
			_ If ball's ycor() is smaller than -300, sety() to -300 and change bearing by a specific degree
		+ Left and right borders upon hit will increase the player's score
			_ If ball's xcor() is larger than 400, setx() to 400 and change bearing by a specific degree, increase player 1's score by 1 (one).
			_ If ball's xcor() is smaller than -400, setx() to -400 and change bearing by a specific degree, increase player 2's score by 1 (one).
	- Step 9: Paddles collisions:
		+ If ball's xcor() and ycor() is in range of paddle's surface, change bearing by a specific degree.
	- Step 10: Anti-voiding the paddles:
		+ If paddles' ycor() is more than 260, sety() back to 260.
		+ If paddles' ycor() is less than -260, sety() back to -260.

## Seven Segments Display
	- Each digit can be displayed by 7 "segments".
	![Examples of seven-segments digits](https://github.com/nguyenhuyblyat/turtle-pong/blob/main/7seg1.gif?raw=true)
	- Based on that, we can work out the following table, which describes which segment to be illuminated to create the digit that we wanted:
	| 	| a | b | c | d | e | f | g |
	|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
	| 0 | x | x | x | x | x | x | o |
	| 1 | o | x | x | o | o | o | o |
	| 2 | x | x | o | x | x | o | x |
	| 3 | x | x | x | x | o | o | x |
	| 4 | o | x | x | o | o | x | x |
	| 5 | x | o | x | x | o | x | x | 
	| 6 | x | o | x | x | x | x | x |
	| 7 | x | x | x | o | o | o | o |
	| 8 | x | x | x | x | x | x | x |
	| 9 | x | x | x | x | o | x | x |
	key: x = on, o = off

	- We can then apply this function that I stole from a chinese website i dont remember lol:
	![lol](https://github.com/nguyenhuyblyat/turtle-pong/blob/main/seven-segment-example.jpg?raw=true)