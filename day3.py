import sys

lines = list(line.strip() for line in sys.stdin)

w, h = len(lines[0]), len(lines)

def slope(xd, yd):
    x, y = 0, 0
    count = 0
    while y < h:
        if lines[y][x] == '#':
            count += 1
        x += xd
        x %= w
        y += yd
    return count

slope1 = slope(1, 1)
slope2 = slope(3, 1)
slope3 = slope(5, 1)
slope4 = slope(7, 1)
slope5 = slope(1, 2)

print(slope2)

print(slope1 * slope2 * slope3 * slope4 * slope5)
