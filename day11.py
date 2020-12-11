import sys

seats = set()

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == 'L':
            seats.add((x, y))

width = x + 1
height = y + 1

def simulate(neighbourhood, tolerance):
    occupied = set()

    while True:
        occupy = set(occupied)

        for seat in seats:
            occupied_neighbours = neighbourhood(seat) & occupied
            if seat not in occupied:
                if not occupied_neighbours:
                    occupy.add(seat)
            else:
                if len(occupied_neighbours) >= tolerance:
                    occupy.remove(seat)

        if occupied == occupy:
            break

        occupied = occupy

    return occupied

directions = ((-1, -1), ( 0, -1), (+1, -1),
              (-1,  0),           (+1,  0),
              (-1, +1), ( 0, +1), (+1, +1))

def moore_neighbourhood(seat):
    x, y = seat
    neighbours = set()
    for xd, yd in directions:
        neighbour = (x + xd, y + yd)
        if neighbour in seats:
            neighbours.add(neighbour)
    return neighbours

print(len(simulate(moore_neighbourhood, 4)))

def sight_neighbourhood(seat):
    x, y = seat
    neighbours = set()
    for xd, yd in directions:
        nx = x + xd
        ny = y + yd
        while nx >= 0 and nx < width and ny >= 0 and ny < height:
            neighbour = (nx, ny)
            if neighbour in seats:
                neighbours.add(neighbour)
                break
            nx += xd
            ny += yd
    return neighbours

print(len(simulate(sight_neighbourhood, 5)))
