import re

from tictoc import tic, toc


def parse(file):
    return file.read()


with open("ex03.txt") as file:
    ex = parse(file)

with open("input03.txt") as file:
    inp = parse(file)

tic()
# -------- Part 1 -----------
print('   PART 1')
result = 0
groups = re.findall(pattern=r'mul\((\d*),(\d*)\)', string=inp)
for group in groups:
    result += int(group[1]) * int(group[0])

print(result)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

result = 0
tokens = [
    "do()",
    "don't()",
    "mul("
]

s = inp
enabled = True
i = 0
while i < len(s):
    for token in tokens:
        for j in range(len(token)):
            if not s[i + j] == token[j]:
                break
            if j == len(token) - 1:
                i += j
                if token == "do()":
                    enabled = True
                elif token == "don't()":
                    enabled = False
                elif token == "mul(" and enabled:
                    k = 1
                    left = ''
                    while s[i + k].isdigit():
                        left += s[i + k]
                        k += 1
                    sep = s[i + k]
                    k += 1
                    right = ''
                    while s[i + k].isdigit():
                        right += s[i + k]
                        k += 1
                    closing = s[i + k]
                    if left and sep == ',' and right and closing == ')':
                        result += int(left) * int(right)
                        i += k
    i += 1

print(result)

toc('Part 2 done in')
