# Cog-SUP 1st Semester Coding Competition: BATTLESHIP

## Overview

Refer to `battleship.pdf` to find the official rules of the game. In this computational version of Battleship, you're going to code the behavior of one player (i.e. one _strategy_), represented by the class `GameStrategy`. Specifically, you're going to code a _subclass_ overwriting two class methods:

1. `setup_board()`: Place your ships at the beginning of a round.
2. `next_move()`: Given your previous moves (as well as their respective results), return a new move.
   A strategy is written in its own file, importing the mother class and defining a daughter class (i.e. extending `GameStrategy`).
   The file `game.py` is an executable python file which gets passed two strategy file names as runtime parameters, and which then simulates a game of Battleship between those two strategies.

For example, to run a game between the strategies `my_strategy.py` and `random_strategy.py`, assuming you're at the root of the repository, run this command in your terminal:
`python .\code\game.py .\code\strategies\my_strategy.py .\code\strategies\random_strategy.py`

**TODO** talk about how the result of the game is logged and how that is used to run a tournament

## The `setup_board()` method:

**TODO** describe more in detail the method signature and how to return your placements

## The `next_move()` method:

**TODO** explain what information is given and what needs to be returned

## The `helper.py` file

**TODO** explain the functions defined in it and that they can be used by your strategy.

## Running a tournament

**TODO** explain how to run a tournament
