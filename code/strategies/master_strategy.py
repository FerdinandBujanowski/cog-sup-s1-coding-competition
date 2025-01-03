class GameStrategy():

    def __init__(self):
        self.moves = []

    def next_move(self):
        raise NotImplementedError("Subclasses should implement this method.")