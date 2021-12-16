from tictoc import tic, toc

tic()

with open("input2.txt") as input_file:
    input_list = [(line.split(' ')[0], int(line.split(' ')[1])) for line in input_file]

# print(input_list)
# -------- Part 1 -----------
print('PART 1')

horizontal = 0
depth = 0
for command in input_list:
    if command[0] == 'forward':
        horizontal += command[1]
    elif command[0] == 'up':
        depth -= command[1]
    elif command[0] == 'down':
        depth += command[1]

result = depth * horizontal

print('horizontal = ', horizontal)
print('depth = ', depth)
print('result = ', result)

# -------- Part 2 -----------
print('PART 2')

horizontal = 0
depth = 0
aim = 0
for command in input_list:
    if command[0] == 'forward':
        horizontal += command[1]
        depth += command[1] * aim
    elif command[0] == 'up':
        aim -= command[1]
    elif command[0] == 'down':
        aim += command[1]

result = depth * horizontal

print('horizontal = ', horizontal)
print('depth = ', depth)
print('result = ', result)

toc()
