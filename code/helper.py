coordinates_x = list(range(1, 11))
coordinates_y = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

HIT, MISS, SUNK, DEFEAT = "H", "M", "S", "D"

SHIP_SIZES = [2, 3, 3, 4, 5]

def ship_tuples(setup: list[tuple[str, int, bool]]) -> list[set[tuple[str, int]]]:
    ships = []

    for placement, size in zip(setup, SHIP_SIZES):
        current_ship = set()

        y, x, hor = placement
        if hor:
            x_index = coordinates_x.index(x)
            if x_index + size > len(coordinates_x):
                # ship beyond game bounds
                return []
            cX = coordinates_x[x_index : x_index + size]
            for cx in cX:
                current_ship.add((y, cx))
        else:
            y_index = coordinates_y.index(y)
            if y_index + size > len(coordinates_y):
                # ship beyond game bounds
                return []
            cY = coordinates_y[y_index : y_index + size]
            for cy in cY:
                current_ship.add((cy, x))

        ships.append(current_ship)

    return ships
    

def check_board_valid(setup: list[tuple[str, int, bool]]) -> bool:
    # 1st: check if correct length
    if len(setup) != len(SHIP_SIZES):
        return False

    # 2nd: check no overlaps
    all_tuples = set()

    ships = ship_tuples(setup=setup)
    for ship in ships:
        for t in ship:
            all_tuples.add(t)

    # no overlaps if amount of tuples == total ship lengths
    return len(all_tuples) == sum(SHIP_SIZES)

def eval_move(setup:list[tuple[str, int, bool]], prev_moves:list[tuple[str, int, str]], current_move:tuple[str, int]) -> str:

    prev_coordinates = [(y, x) for (y, x, _) in prev_moves]
    
    # always return MISS when current move already played before
    if current_move in prev_coordinates:
        return MISS
    
    ships = ship_tuples(setup=setup)

    # 1st loop: remove already hit coordinates
    for ship in ships:
        to_be_removed = []
        for t in ship:
            if t in prev_coordinates:
                to_be_removed.append(t)
        for t in to_be_removed:
            ship.remove(t)
    
    # 2nd loop: check for new hit among remaining ship parts
    for ship in ships:
        if current_move in ship:
            if len(ship) > 1:
                return HIT
            # only one ship part left: game is lost
            if sum([len(s) for s in ships]) == 1:
                return DEFEAT
            return SUNK
    return MISS