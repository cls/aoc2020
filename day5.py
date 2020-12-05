import sys

def boarding_pass_seat(boarding_pass):
    seat = 0

    for letter in boarding_pass:
        seat <<= 1
        seat |= letter in ('B', 'R')

    return seat

seats = set(boarding_pass_seat(line.strip()) for line in sys.stdin)

print(max(seats))

seat = min(seats)

while seat in seats:
    seat += 1

print(seat)
