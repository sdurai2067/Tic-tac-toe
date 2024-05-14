Tic Tac Toe Game

Description:
This Python script implements a simple Tic Tac Toe game using the tkinter library for the graphical user interface. Players take turns clicking on squares in a 3x3 grid to place their marks (X or O). The game tracks player scores and allows for restarting the game or continuing to the next round.

Features:

Graphical user interface built with tkinter.
Supports two players (X and O).
Tracks player scores.
Allows for restarting the game or continuing to the next round.
Draws the Tic Tac Toe board dynamically.
Detects winning combinations and draws.

File Structure:

tictactoe.py: The main Python script containing the Tic Tac Toe game implementation.
xo logo.png: Image file used for the game logo.

How to Run:

Ensure you have Python installed on your system.
Install the required libraries: tkinter and Pillow (pip install tkinter Pillow).
Run the tictactoe.py script using Python.
Game Instructions:

Click on any empty square to place your mark (X or O).
The game alternates between players after each move.
The first player to form a horizontal, vertical, or diagonal line wins.
If no player wins and the board is full, the game declares a draw.
Use the "RESTART" button to reset player scores and start a new game.
Use the "CONTINUE" button to start a new round without resetting player scores.
Block diagram:
        Start
|
V
Initialize Game
|
V
Draw Game Board
|
V
Loop until game ends:
|   |
|   V
|   Player Makes Move
|   |
|   V
|   Check for Winner
|   |
|   V
|   If Winner:
|   |   |
|   |   V
|   |   Display Winner
|   |
|   V
|   If Draw:
|   |   |
|   |   V
|   |   Display Draw
|   |
|   V
|   Switch Player
|
V
End Game
|
V
Display Final Scores
|
V
Option to Restart or Continue
|
V
End

Additional Notes:

The game board is dynamically drawn using tkinter's Canvas widget.
Player scores are displayed at the top of the window.
The game logo is displayed at the top-center of the window.

*Enjoy playing Tic Tac Toe! 🎮*
