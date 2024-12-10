from tictoc import tic, toc


def parse(file):
    return [[int(e) for e in line.strip().split()] for line in file if line.strip() != '']


with open("ex02.txt") as file:
    ex = parse(file)

with open("input02.txt") as file:
    inp = parse(file)

print(ex)

tic()
# -------- Part 1 -----------
print('   PART 1')
result = 0

for line in inp:
    safe = True
    increasing = line[0] - line[1] <= 0
    for i in range(len(line) - 1):
        diff = line[i] - line[i + 1]
        if (diff <= 0) != increasing or not 1 <= abs(diff) <= 3:
            safe = False
            break
    if safe:
        result += 1

print(result)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')


def is_safe(report):
    safe = True
    increasing = report[0] - report[1] <= 0
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if (diff <= 0) != increasing or not 1 <= abs(diff) <= 3:
            return False
    return True


result = 0

for line in inp:
    if is_safe(line):
        result += 1
    else:
        for i in range(len(line)):
            new_report = line[:]
            new_report.pop(i)
            if is_safe(new_report):
                result += 1
                break

print(result)

toc('Part 2 done in')
