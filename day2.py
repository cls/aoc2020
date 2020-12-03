import re
import sys

pattern = re.compile(r'([1-9]*[0-9])-([1-9]*[0-9]) ([a-z]): ([a-z]+)')

valid1 = 0
valid2 = 0

for line in sys.stdin:
    match = pattern.match(line)

    minimum = int(match.group(1))
    maximum = int(match.group(2))
    required = match.group(3)
    password = match.group(4)

    count = 0
    for char in password:
        if char == required:
            count += 1

    if count >= minimum and count <= maximum:
        valid1 += 1

    if (password[minimum - 1] == required) != (password[maximum - 1] == required):
        valid2 += 1

print(valid1)
print(valid2)
