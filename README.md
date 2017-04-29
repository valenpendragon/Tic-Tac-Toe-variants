# Tic-Tac_Toe-variants
To play this game, you need to download only one of two files. For the Jupyter Notebook prototype, use Tic-Tac-Toe.ipynb. Do a Run All Cells to start the game.
For a Python interactive version, use Tic-Tac-Toe.py.

This project is currently written in Python 2.7.13.

I am open to suggestions for the name for the game once it supports a more streamlined, Pente or go moku style flavor.

Note: This a human player game on a single terminal currently. This does not have a computer player built-in.
-----------------------------------------------------------------------------------------------------------------------------
This started out as a project for a Python bootcamp, but I decided it would be cool to eventually evolve it into multiplayer
go moku, Pente, or even variants of Connect-4.

Currently, it is a prototype for two players, but the foundation for large numbers of players is already there. It is on my
list to implement soon.

This Tic-Tac-Toe version uses a multilayer dictionary to sort sets of winning moves. It uses a set to store open spaces remaining
on the board. It uses a single layer dictionary to assign sets of players moves to the key, the player's name.

Right now, it is primarily a terminal game, although it can be played in iPython as well (use the Jupyter notebook version). It 
supports boards up to 9x9, but once I learn more about GUI development in Python, expect that to change.

------------------------------------------------------------------------------------------------------------------------------
Current Development
------------------------------------------------------------------------------------------------------------------------------
Moving the player_moves initialization to a function in order to enable players up to (size - 1), where size is the lenght of 
a side of the square board.

------------------------------------------------------------------------------------------------------------------------------
Change Log
------------------------------------------------------------------------------------------------------------------------------
4/27/17: Working two player prototype with groundwork for unlimited player and board size.

------------------------------------------------------------------------------------------------------------------------------
Someday
------------------------------------------------------------------------------------------------------------------------------
Two dimensional GUI with up 64x64 board size with victory conditions any straight chain from 3 up to 64.
Three dimensionalr GUI (yes really, this is someday stuff) with a rotatable cube.
