import sys

card_key = int(next(sys.stdin))
door_key = int(next(sys.stdin))

def transform(subject):
    value = 1
    while True:
        yield value
        value *= subject
        value %= 20201227

for loop, key in enumerate(transform(7)):
    if key == card_key:
        break

card_loop = loop

for loop, key in enumerate(transform(door_key)):
    if loop == card_loop:
        break

private_key = key

print(private_key)
