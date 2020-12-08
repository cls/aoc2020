import sys

program = []

for line in sys.stdin:
    op, num = line.split()
    program.append((op, int(num)))

class Machine:
    def __init__(self, code):
        self.pc = 0
        self.acc = 0
        self.code = code
        self.visited = set()

    def step(self):
        if self.pc == len(self.code): # terminates
            return True

        if self.pc in self.visited: # infinite loop
            return False

        self.visited.add(self.pc)

        op, num = self.code[self.pc]
        if op == 'acc':
            self.acc += num
            self.pc += 1
        elif op == 'jmp':
            self.pc += num
        elif op == 'nop':
            self.pc += 1

    def run(self):
        while True:
            result = self.step()
            if result is not None:
                return result

machine = Machine(program)
machine.run()

print(machine.acc)

for i, (op, num) in enumerate(program):
    if op == 'acc':
        continue
    elif op == 'jmp':
        program[i] = ('nop', num)
    elif op == 'nop':
        program[i] = ('jmp', num)

    machine = Machine(program)
    if machine.run():
        break

    program[i] = (op, num) # restore original instruction

print(machine.acc)
