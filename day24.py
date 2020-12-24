import sys

directions = {
    'e':  (+1, -1),
    'se': ( 0, -1),
    'sw': (-1,  0),
    'w':  (-1, +1),
    'nw': ( 0, +1),
    'ne': (+1,  0),
}

def get_neighbour(cell, direction):
    x, y = cell
    xd, yd = directions[direction]
    return x+xd, y+yd

tiles = set()

for line in sys.stdin:
    tile = (0, 0)
    direction = ''
    for char in line.strip():
        direction += char
        if direction in directions:
            tile = get_neighbour(tile, direction)
            direction = ''
    tiles ^= {tile}

print(len(tiles))

def evaluate(state):
    neighbours = {}

    for cell in state:
        for direction in directions:
            neighbour = get_neighbour(cell, direction)
            neighbours[neighbour] = neighbours.get(neighbour, 0) + 1

    new_state = set()

    for cell, count in neighbours.items():
        if count == 2 or (cell in state and count == 1):
            new_state.add(cell)

    return new_state

for day in range(100):
    tiles = evaluate(tiles)

print(len(tiles))
