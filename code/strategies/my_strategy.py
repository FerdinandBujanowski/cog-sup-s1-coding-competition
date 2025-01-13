from strategies.master_strategy import GameStrategy
from helper import coordinates_x, coordinates_y, SHIP_SIZES

# you can rename the class, as long as it extends GameStrategy
class MyStrategy(GameStrategy):

    def __init__(self):
        super().__init__(devname="<Your Name>", stratname="<Your Strategy's Nickname>")

    def setup_board(self) -> list[tuple[str, int, bool]]:

        # TODO code your own board setup
        return [(letter, 1, True) for letter, _ in zip(coordinates_y, SHIP_SIZES)] # example code

    def next_move(self, prev_moves:list[tuple[str, int, str]]) -> tuple[str, int]:

        # TODO code your own strategy
        return (coordinates_y[0], coordinates_x[0]) # example code