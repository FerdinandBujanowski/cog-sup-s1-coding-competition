from helper import coordinates_x, coordinates_y

class GameStrategy():

    def __init__(self, devname, stratname):
        self.devname = devname
        self.stratname = stratname

    # ship order follows order of constants.py
    def setup_board() -> list[tuple[str, int, bool]]:
        raise NotImplementedError("Subclasses should implement this method.")

    def next_move(self, prev_moves:list[tuple[str, int, str]]) -> tuple[str, int]:
        raise NotImplementedError("Subclasses should implement this method.")