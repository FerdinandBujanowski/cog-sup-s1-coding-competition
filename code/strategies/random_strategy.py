from strategies.master_strategy import GameStrategy
import random

from helper import coordinates_x, coordinates_y, SHIP_SIZES
from helper import check_board_valid

class RandomStrategy(GameStrategy):

    def __init__(self):
        super().__init__(devname="Max Mustermann", stratname="Random Strategy")

    def setup_board(self) -> list[tuple[str, int, bool]]:
        valid = False
        setup = None
        # VERY BAD CODING PRACTICE
        while not valid:
            setup = [(random.choice(coordinates_y), random.choice(coordinates_x), random.choice([True, False])) for _ in SHIP_SIZES]
            valid = check_board_valid(setup)
        return setup

    def next_move(self, prev_moves:list[tuple[str, int, str]]) -> tuple[str, int]:
        return (random.choice(coordinates_y), random.choice(coordinates_x))