import itertools

from tictoc import tic, toc


def parse(file):
    inp = [tuple([int(e) for e in s.split(' ')]
                 for s in line.split(': '))
           for line in file]
    for i, line in enumerate(inp):
        inp[i] = (line[0][0], line[1])
    return inp


with open("ex07.txt") as file:
    ex = parse(file)

with open("input07.txt") as file:
    inp = parse(file)

tic()
# -------- Part 1 -----------
print('   PART 1')
s = inp
operators = ['+', '*']
result = 0

for line in s:
    test_value = line[0]
    numbers = line[1]
    n_operator = len(numbers) - 1
    ops = itertools.product(operators, repeat=n_operator)
    for op in ops:
        acc = numbers[0]
        for i in range(len(op)):
            if op[i] == '+':
                acc += numbers[i + 1]
            elif op[i] == '*':
                acc *= numbers[i + 1]
            else:
                raise ValueError('invalid operator')
        if acc == test_value:
            result += test_value
            break

print(result)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

s = inp
operators = ['+', '*', '||']
result = 0

for line in s:
    test_value = line[0]
    numbers = line[1]
    n_operator = len(numbers) - 1
    ops = itertools.product(operators, repeat=n_operator)
    for op in ops:
        acc = numbers[0]
        for i in range(len(op)):
            if op[i] == '+':
                acc += numbers[i + 1]
            elif op[i] == '*':
                acc *= numbers[i + 1]
            elif op[i] == '||':
                acc = int(str(acc) + str(numbers[i + 1]))
            else:
                raise ValueError('invalid operator')
            if acc > test_value:
                break
        if acc == test_value:
            result += test_value
            break

print(result)

toc('Part 2 done in')
