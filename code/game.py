import importlib
import sys
import os
import csv
from strategies.master_strategy import GameStrategy

from helper import check_board_valid, eval_move, DEFEAT, MISS

def load_strategies(file_names) -> tuple[GameStrategy, GameStrategy]:
    strats = []
    for file_name in file_names:
        module_name = os.path.splitext(os.path.basename(file_name))[0]
        full_module_name = f"strategies.{module_name}"  # Include the package name
        try:
            # Dynamically import the module
            module = importlib.import_module(full_module_name)
            
            # Find subclasses of GameStrategy in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, GameStrategy) and attr is not GameStrategy:
                    # Instantiate and call the method
                    instance = attr()
                    strats.append(instance)
        except Exception as e:
            print(f"Error loading strategy {full_module_name}: {e}")

    return strats[0], strats[1]

def print_winner(strat:GameStrategy):
    print("The winner is strategy " + strat.stratname + ", programmed by " + strat.devname)

if __name__ == "__main__":
    # Pass file names as runtime parameters

    # Collect file names from command-line arguments
    file_names = sys.argv[1:]  

    # get logger file name
    log_file_name = "gamelog"
    if len(file_names) >= 3:
        log_file_name = file_names[2]

    # load strategies
    strat1, strat2 = load_strategies(file_names[:2])

    with open(log_file_name + ".csv", "w", newline="") as logfile:
        
        # create logger
        logger = csv.writer(logfile)

        # run game between two strategies
        
        # both strats set up their boards
        board_s1 = strat1.setup_board()
        board_s2 = strat2.setup_board()

        winner = 0

        # check if boards are properly set up, disqualify if not
        if not check_board_valid(board_s1):
            print("Board 1 setup not valid.")
            winner = 2
        
        if not check_board_valid(board_s2):
            print("Board 2 setup not valid.")
            if winner == 2:
                winner = 0.5
            else:
                winner = 1

        # main part of the game
        s1_moves = []
        s1_points = 0

        s2_moves = []
        s1_points = 0

        while winner == 0:
            # s1 plays first
            current_move_s1 = strat1.next_move(s1_moves)
            eval_s1 = eval_move(setup=board_s2, prev_moves=s1_moves, current_move=current_move_s1)
            s1_moves.append((current_move_s1[0], current_move_s1[1], eval_s1))

            # print(strat1.stratname + " plays " + current_move_s1[0] + str(current_move_s1[1]) + ": " + eval_s1)
            logger.writerow([1, current_move_s1[0], current_move_s1[1], eval_s1, 0])

            # s2 plays second
            current_move_s2 = strat2.next_move(s2_moves)
            eval_s2 = eval_move(setup=board_s1, prev_moves=s2_moves, current_move=current_move_s2)
            s2_moves.append((current_move_s2[0], current_move_s2[1], eval_s2))

            # print(strat2.stratname + " plays " + current_move_s2[0] + str(current_move_s2[1]) + ": " + eval_s2)
            logger.writerow([2, current_move_s2[0], current_move_s2[1], eval_s2, 0])

            if eval_s1 == DEFEAT:
                winner = 1
            if eval_s2 == DEFEAT:
                if winner == 1:
                    # draw
                    winner = 0.5
                else:
                    winner = 2

        logger.writerow([0, 0, 0, 0, winner])
        if winner == 0.5:
            print("Draw")
        elif winner == 1:
            print_winner(strat1)
        else:
            print_winner(strat2)

    # TODO log winner into file for tournament