import sys

def product_of_sum_to(target, values):
    for value in values:
        complement = target - value
        if complement in values:
            return value * complement

values = set(int(line) for line in sys.stdin)

print(product_of_sum_to(2020, values))

for value in values:
    subproduct = product_of_sum_to(2020 - value, values)
    if subproduct:
        print(value * subproduct)
        break
