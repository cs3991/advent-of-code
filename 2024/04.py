from tictoc import tic, toc


def parse(file):
    return [[c for c in line.strip()] for line in file]


with open("ex04.txt") as file:
    ex = parse(file)

with open("input04.txt") as file:
    inp = parse(file)

tic()
# -------- Part 1 -----------
print('   PART 1')
pattern = 'XMAS'

directions = [
    (1, -1),
    (1, 0),
    (1, 1),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]

result = 0

s = inp
for y in range(len(s)):
    line = s[y]
    for x in range(len(line)):
        c = line[x]
        for dx, dy in directions:
            if not (0 <= x + (len(pattern) - 1) * dx < len(line)
                    and 0 <= y + (len(pattern) - 1) * dy < len(s)): continue
            pattern_found = True
            for i in range(len(pattern)):
                if s[y + i * dy][x + i * dx] != pattern[i]:
                    pattern_found = False
                    break
            if pattern_found:
                result += 1
print(result)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
patterns = [
    ["M.S",
     ".A.",
     "M.S"],
    ["M.M",
     ".A.",
     "S.S"],
    ["S.S",
     ".A.",
     "M.M"],
    ["S.M",
     ".A.",
     "S.M"],
]
result = 0

s = inp
for y in range(len(s) - 2):
    line = s[y]
    for x in range(len(line) - 2):
        c = line[x]
        for pattern in patterns:
            pattern_found = True
            for dy in range(3):
                for dx in range(3):
                    if pattern[dy][dx] != '.' and s[y + dy][x + dx] != pattern[dy][dx]:
                        pattern_found = False
                        break
                if not pattern_found:
                    break
            if pattern_found:
                result += 1
                break

print(result)

toc('Part 2 done in')
