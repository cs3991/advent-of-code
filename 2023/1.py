# from collections import defaultdict, Counter
from tictoc import tic, toc
# from cprint import cprint

tic()

with open("ex1.txt") as file:
    ex = [line for line in file]

with open("input1.txt") as file:
    inp = [line for line in file]
# print(inp)

# -------- Part 1 -----------
print('   PART 1')
solution = 0
calibr_values = []
for line in inp:
    buffer = ''
    for char in line:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            buffer+=char
            break
    for char in line[::-1]:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            buffer += char
            break
    solution += int(buffer)

print(solution)
toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')
lut = {
'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
}
solution = 0
calibr_values = []
for line in inp:
    first = None
    last = None
    line_length = len(line)
    for i in range(len(line)):
        char = line[i]
        for pattern in lut.keys():
            j = 0
            while i + j < line_length and j < len(pattern) and line[i + j] == pattern[j]:
                if j == len(pattern) - 1:
                    if first is None:
                        first = lut[pattern]
                    last = lut[pattern]
                j += 1

    solution += int(first + last)

print(solution)


toc('Partie 2 terminée en')
