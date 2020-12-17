import itertools
import sys

state_2d = set()

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == '#':
            state_2d.add((x, y))

def evaluate(state):
    neighbours = {}

    for cell in state:
        for neighbour in itertools.product(*((n-1, n, n+1) for n in cell)):
            neighbours[neighbour] = neighbours.get(neighbour, 0) + 1

    new_state = set()

    for cell, count in neighbours.items():
        if count == 3 or (cell in state and count == 4): # counts active state itself
            new_state.add(cell)

    return new_state

state_3d = set((x, y, 0) for x, y in state_2d)

for step in range(6):
    state_3d = evaluate(state_3d)

print(len(state_3d))

state_4d = set((x, y, 0, 0) for x, y in state_2d)

for step in range(6):
    state_4d = evaluate(state_4d)

print(len(state_4d))
