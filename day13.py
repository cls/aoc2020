import math
import sys

departure = int(sys.stdin.readline())

buses = {i: int(bus) for i, bus in enumerate(sys.stdin.readline().split(',')) if bus != 'x'}

def time_to_wait(bus):
    return bus - (departure % bus)

earliest_bus = min(buses.values(), key=time_to_wait)

print(earliest_bus * time_to_wait(earliest_bus))

def lcm(x, y): # Added to stdlib in Python 3.9
    return x * y // math.gcd(x, y)

time = 0
rep = 1

for pos, bus in buses.items():
    while (time + pos) % bus != 0:
        time += rep
    rep = lcm(rep, bus)

print(time)
