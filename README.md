# Cog-SUP 1st Semester Coding Competition: BATTLESHIP

## Overview

Refer to `battleship.pdf` to find the official rules of the game. In this computational version of Battleship, you're going to code the behavior of one player (i.e. one _strategy_), represented by the class `GameStrategy`. Specifically, you're going to code a _subclass_ overwriting two class methods:

1. `setup_board()`: Place your ships at the beginning of a round.
2. `next_move()`: Given your previous moves (as well as their respective results), return a new move.
   A strategy is written in its own file, importing the mother class and defining a daughter class (i.e. extending `GameStrategy`).

The file `game.py` is an executable python file which gets passed two strategy file names as runtime parameters, and which then simulates a game of Battleship between those two strategies.
For example, to run a game between the strategies `my_strategy.py` and `random_strategy.py`, assuming you're at the root of the repository, run this command in your terminal:
`python .\code\game.py .\code\strategies\my_strategy.py .\code\strategies\random_strategy.py`
A log file (in CSV format) will automatically be generated. This log file will be used during the tournament to keep track of who beat who (a `tournament.py` file will be created at a later time).

## The `setup_board()` method:

As you can see from the method signature, this method needs to return a list of (string, int, boolean)-tuples, each tuples representing the position and orientation of one of the players ships. There are **five ships** in total (of lengths 2, 3, 3, 4 and 5, respectively), so the returned list needs to be of length 5. The tuple at position i in the list corresponds to the position / orientation of ship i.

1. The first element of the tuple corresponds to the **y-coordinate** of one end of the given ship (capital letter from A to J).
2. The second element of the tuple corresponds to the **x-coordinate** of that same end of the given ship (integer from 1 to 10 included).
3. The third element corresponds to the **orientation** of the given ship (`True`= horizontal, the declared coordinates define the **left end** of the given ship, `False`= vertical, the declared coordinates define the **top end** of the given ship).

## The `next_move()` method:

**TODO** explain what information is given and what needs to be returned

## The `helper.py` file

**TODO** explain the functions defined in it and that they can be used by your strategy.

## Running a tournament

**TODO** explain how to run a tournament
