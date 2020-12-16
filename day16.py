import sys

fields = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    key, ranges_s = line.split(': ')
    ranges = []
    for range_s in ranges_s.split(' or '):
        min_s, max_s = range_s.split('-')
        ranges.append((int(min_s), int(max_s)))
    fields[key] = ranges

next(sys.stdin) # "your ticket:"

my_ticket = tuple(map(int, next(sys.stdin).split(',')))

next(sys.stdin) # ""
next(sys.stdin) # "nearby tickets:"

nearby_tickets = [tuple(map(int, line.split(','))) for line in sys.stdin]

def possible_fields_for_value(value):
    possibilities = set()
    for key, ranges in fields.items():
        if any(value >= min and value <= max for min, max in ranges):
            possibilities.add(key)
    return possibilities

error_rate = 0
possible_fields = [set(fields.keys()) for value in my_ticket]

for ticket in nearby_tickets:
    possible_fields_for_ticket = [possible_fields_for_value(value) for value in ticket]
    if all(possible_fields_for_ticket):
        for possibilities, possibilities_for_ticket in zip(possible_fields, possible_fields_for_ticket):
            possibilities &= possibilities_for_ticket
    else:
        for value, possibilities_for_ticket in zip(ticket, possible_fields_for_ticket):
            if not possibilities_for_ticket:
                error_rate += value

print(error_rate)

field_names = [None for value in my_ticket]

while not all(field_names):
    for i, possibilities in enumerate(possible_fields):
        if len(possibilities) == 1:
            possibility = possibilities.pop()
            field_names[i] = possibility
            for other_possibilities in possible_fields:
                other_possibilities.discard(possibility)

labelled_ticket = dict(zip(field_names, my_ticket))

departure_product = 1
for key, value in labelled_ticket.items():
    if key.startswith('departure'):
        departure_product *= value

print(departure_product)
