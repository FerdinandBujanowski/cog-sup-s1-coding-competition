from strategies.master_strategy import GameStrategy

class RandomStrategy(GameStrategy):

    def __init__(self):
        super().__init__()

    def next_move(self):
        print("Random Strategy next move.")