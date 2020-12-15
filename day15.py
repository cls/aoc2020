import sys

def play(nums, turns):
    last_spoken = {}

    turn = 1
    num = nums[0]

    while turn < turns:
        if turn < len(nums):
            next_num = nums[turn]
        elif num in last_spoken:
            next_num = turn - last_spoken[num]
        else:
            next_num = 0

        last_spoken[num] = turn

        turn += 1
        num = next_num

    return num

starting_numbers = list(map(int, sys.stdin.read().split(',')))

print(play(starting_numbers, 2020))

print(play(starting_numbers, 30000000))
