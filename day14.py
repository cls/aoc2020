import re
import sys

pattern = re.compile(r'(mask|mem\[([1-9][0-9]*)\]) = ([1-9][0-9]*|[01X]+)')

program = [pattern.fullmatch(line.strip()).groups() for line in sys.stdin]

memory = {}

for dest, addr, value in program:
    if dest == 'mask':
        mask_and = 0
        mask_or = 0
        for char in value:
            mask_and <<= 1
            mask_or <<= 1
            if char == 'X':
                mask_and |= 1
            elif char == '1':
                mask_or |= 1
    else:
        memory[int(addr)] = (int(value) & mask_and) | mask_or

print(sum(memory.values()))

def subaddrs(masked_addr):
    prefix, x, suffix = masked_addr.partition('X')
    if x:
        for subaddr in subaddrs(suffix):
            yield prefix + '0' + subaddr
            yield prefix + '1' + subaddr
    else:
        yield prefix

memory = {}

for dest, addr, value in program:
    if dest == 'mask':
        mask = value
    else:
        bin_addr = '{:036b}'.format(int(addr))
        masked_addr = ''.join(addr_bit if mask_bit == '0' else mask_bit for mask_bit, addr_bit in zip(mask, bin_addr))
        for subaddr in subaddrs(masked_addr):
            memory[int(subaddr, 2)] = int(value)

print(sum(memory.values()))
