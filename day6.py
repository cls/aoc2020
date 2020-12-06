import sys

def read_groups(lines):
    group = []
    for line in lines:
        line = line.strip()
        if line:
            group.append(set(line))
        elif group:
            yield group
            group = []
    if group:
        yield group

groups = list(read_groups(sys.stdin))

anyone = sum(len(set.union(*group)) for group in groups)

print(anyone)

everyone = sum(len(set.intersection(*group)) for group in groups)

print(everyone)
