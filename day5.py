import sys

num_seats = 128 * 8

def boarding_pass_seat(boarding_pass):
    lower = 0
    upper = num_seats
    delta = num_seats // 2

    for letter in boarding_pass:
        if letter in ('B', 'R'):
            lower += delta
        else:
            upper -= delta
        delta //= 2

    assert lower == upper - 1

    return lower

seats = set()

for line in sys.stdin:
    seat = boarding_pass_seat(line.strip())
    seats.add(seat)

print(max(seats))

middle = False

for seat in range(num_seats):
    if seat in seats:
        middle = True
    elif middle:
        break

print(seat)
