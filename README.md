The famous "Pong!" game, recreated in Python 3.9.2 with built-in Turtle library.	

Note: This program is released under GNU General Public License version 3, all forks of this program are allowed as long as they are open-source. Full version of the license can be found in the repository under the name `LICENSE`.

## Prerequisites
	- Python 3.x (https://python.org/)
	- Turtle (built-in within Python)
	- random (built-in within Python)

## Running
	- `python3 main.py`
	- `python main.py` if the above doesn't work (edge cases)

## Controls
	- Player 1 (left): A for up, Z for down
	- Player 2 (right): K for up, M for down
	- Quit: Y

## Magic Hax
	- Step 1: Create an 800x600 window with Turtle, with a black background.
	- Step 2: Create the net between two players.
	- Step 3: Create the paddles and the ball to hit with.
		+ Move the paddles to near the left and right border of the screen
		+ The ball stays at [0, 0]
	- Step 4: Define functions to move the paddles, and to quit the game
		+ Paddle 1 up, down
		+ Paddle 2 up, down
		+ Quiting the game
	- Step 5: Create a scoring system:
		+ Step 5.1: Initialize player 1's and player 2's score (0  -  0)
		+ Step 5.2: Create a turtle Object and write the variables to it, using .format() function.
		+ Step 5.3: Display the scoreboard on top of the screen
	- Step 6: Borders collisions:
		+ Upper and lower borders will bounce the ball off
			_ If ball's ycor() is larger than 300, sety() to 300 and change bearing by a specific degree
			_ If ball's ycor() is smaller than -300, sety() to -300 and change bearing by a specific degree
		+ Left and right borders upon hit will increase the player's score
			_ If ball's xcor() is larger than 400, setx() to 400 and change bearing by a specific degree, increase player 1's score by 1 (one).
			_ If ball's xcor() is smaller than -400, setx() to -400 and change bearing by a specific degree, increase player 2's score by 1 (one).
	- Step 7: Paddles collisions:
		+ If ball's xcor() and ycor() is in range of paddle's surface, change bearing by a specific degree.
	- Step 8: Anti-voiding the paddles:
		+ If paddles' ycor() is more than 260, sety() back to 260.
		+ If paddles' ycor() is less than -260, sety() back to -260.