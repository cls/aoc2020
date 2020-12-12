import math
import sys

def rotate(x, y, d):
    r = math.radians(d)
    return x * math.cos(r) - y * math.sin(r), x * math.sin(r) + y * math.cos(r)

def manhattan(x, y):
    return round(abs(x) + abs(y))

actions = [(line[0], int(line[1:])) for line in sys.stdin]

x = 0
y = 0
d = 0

for op, num in actions:
    if op == 'N':
        y -= num
    elif op == 'S':
        y += num
    elif op == 'E':
        x += num
    elif op == 'W':
        x -= num
    elif op == 'L':
        d -= num
    elif op == 'R':
        d += num
    elif op == 'F':
        xd, yd = rotate(num, 0, d)
        x += xd
        y += yd

print(manhattan(x, y))

x = 0
y = 0
wx = 10
wy = -1

for op, num in actions:
    if op == 'N':
        wy -= num
    elif op == 'S':
        wy += num
    elif op == 'E':
        wx += num
    elif op == 'W':
        wx -= num
    elif op == 'L':
        wx, wy = rotate(wx, wy, -num)
    elif op == 'R':
        wx, wy = rotate(wx, wy, +num)
    elif op == 'F':
        x += num * wx
        y += num * wy

print(manhattan(x, y))
