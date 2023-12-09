import math

from tictoc import tic, toc

with open("ex08.txt") as file:
    ex = file.readlines()

with open("input08.txt") as file:
    inp = file.readlines()
# inp = ex

tic()
# -------- Part 1 -----------
print('   PART 1')
# Parsing :
nodes = dict()
for i, line in enumerate(inp):
    if i == 0:
        instructions = list(line.strip())
    elif line.strip() == '':
        continue
    else:
        nodes[line.split(' = ')[0]] = line.strip().split(' = (')[1].strip(')').split(', ')


# Algo
def part1(nodes, instructions):
    current_node = 'AAA'
    number_of_steps = 0
    while True:
        for instruction in instructions:
            number_of_steps += 1
            if instruction == 'L':
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]
            if current_node == 'ZZZ':
                return number_of_steps


print(part1(nodes, instructions))
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
# Parsing :
nodes = dict()
for i, line in enumerate(inp):
    if i == 0:
        instructions = list(line.strip())
    elif line.strip() == '':
        continue
    else:
        nodes[line.split(' = ')[0]] = line.strip().split(' = (')[1].strip(')').split(', ')


# Algo
def part2(nodes, instructions):
    current_nodes = []
    for node in nodes.keys():
        if node.endswith('A'):
            current_nodes.append(node)
    solutions = [None for _ in current_nodes]
    for i in range(len(current_nodes)):
        number_of_steps = 0
        node = current_nodes[i]
        while not node.endswith('Z'):
            for instruction in instructions:
                number_of_steps += 1
                if instruction == 'L':
                    node = nodes[node][0]
                else:
                    node = nodes[node][1]
                if node.endswith('Z'):
                    solutions[i] = number_of_steps
                    break
    return (math.lcm(*solutions))


print(part2(nodes, instructions))

toc('Part 2 done in')
