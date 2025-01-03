import importlib
import sys
import os
from strategies.master_strategy import GameStrategy  # Import the base class from the package

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

if __name__ == "__main__":
    # Pass file names as runtime parameters

    # Collect file names from command-line arguments
    file_names = sys.argv[1:]  

    # load strategies
    strat1, strat2 = load_strategies(file_names)

    # run game between two strategies

    # TODO
    strat1.next_move()
    strat2.next_move()
