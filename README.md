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

As you can see from the method signature, this method needs to return a list of (string, int, boolean)-tuples, each tuple representing the position and orientation of one of the players ships. There are **five ships** in total (of lengths 2, 3, 3, 4 and 5, respectively), so the returned list needs to be of length 5. The tuple at position i in the list corresponds to the position / orientation of ship i.

1. The first element of the tuple corresponds to the **y-coordinate** of one end of the given ship (capital letter from A to J).
2. The second element of the tuple corresponds to the **x-coordinate** of that same end of the given ship (integer from 1 to 10 included).
3. The third element corresponds to the **orientation** of the given ship (`True`= horizontal, the declared coordinates define the **left end** of the given ship, `False`= vertical, the declared coordinates define the **top end** of the given ship).

## The `next_move()` method:

This method takes in a list of (string, int, string)-tuples corresponding to your strategy's **previous moves**, and returns a (string, int) tuple corresponding to the next coordinate of your opponent's board that you wish to strike.

1. In the list of previous moves, the first element corresponds to the first move yours strategy did, and the last element corresponds to your strategy's last move (at a given moment). If it is your strategy's first move, then the list will be empty. The first two elements of each tuple (string, int) correspond to the y- and x-coordinates of that respective move. The third element (string) corresponds to the **evaluation** of that respective move; a move can be
   - Hit - _'H'_,
   - Miss - _'M'_,
   - Sunk - _'S'_,
   - and Defeat - _'D'_.
2. The tuple (string, int) that is to be returned corresponds to the y- and x-coordinates of the next piece of the opponent's board that you want to strike. As always, the y-coordinate is a capital letter while the x-coordinate is an integer.

## The `helper.py` file

This file contains some useful constants that you can import into your strategy (coordinates, evaluation characters and ship sizes) as well as some functions used by `game.py` to simulate a game between two strategies. You are free to use these functions as well, in case you deem them useful. For example, `check_board_valid()` checks if a board setup (constellation of ships) has any overlaps or goes beyond the borders of the board. In the case that your strategy returns such an invalid constellation, you will immediately lose the current game.

## Cloning / Submissions

If you want to participate in the coding competition, here's what you need to do:

1. Clone the repository onto your computer (or download a zip file) - no need to create a branch!
2. Modify `my_strategy.py` (You can change the file / class name, as long as the strategy class still extends `GameStrategy`)
3. Once you finished coding your strategy, send the corresponding `.py` file to Ferdinand (via Mail/WhatsApp/Discord/..).

I will gather all strategies and work on some code for the tournament as well as a graphic interface in the meantime.

**The deadline for strategy submissions is the 27th of January!** On the 31st, there will be a "playoff" event where a live tournament between all submitted strategies is being run. More info on that soon..

For now, good luck and have fun coding :)
