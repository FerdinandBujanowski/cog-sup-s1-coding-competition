from strategies.master_strategy import GameStrategy

class DummyStrategy(GameStrategy):

    def __init__(self):
        super().__init__()

    def next_move(self):
        print("Dummy Strategy next move.")