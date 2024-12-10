from tictoc import tic, toc

with open("ex01.txt") as file:
    ex = [tuple(int(e) for e in line.strip().split('   ')) for line in file if line.strip() != '']

with open("input01.txt") as file:
    inp = [tuple(int(e) for e in line.strip().split('   ')) for line in file if line.strip() != '']
# print(ex)

tic()
# -------- Part 1 -----------
print('   PART 1')
left = []
right = []
for line in inp:
    left.append(line[0])
    right.append(line[1])
result = 0

while left:
    left.sort()
    right.sort()
    l = left.pop(0)
    r = right.pop(0)
    result += abs(l - r)

print(result)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

left = []
right = []
for line in inp:
    left.append(line[0])
    right.append(line[1])
result = 0

for l in left:
    result += l * right.count(l)

print(result)
toc('Part 2 done in')
