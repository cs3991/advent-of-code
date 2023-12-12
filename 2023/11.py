import itertools

from tictoc import tic, toc

with open("ex11.txt") as file:
    ex: tuple[tuple[str]] = tuple(tuple(line.strip()) for line in file if line.strip() != '')

with open("input11.txt") as file:
    inp: tuple[tuple[str]] = tuple(tuple(line.strip()) for line in file if line.strip() != '')
# inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')

# Expansion: get the index of empty lines and columns
empty_rows = set()
for y in range(len(inp)):
    if not '#' in inp[y]:
        empty_rows.add(y)

empty_columns = set()
for x in range(len(inp[0])):
    empty_column = True
    for y in range(len(inp)):
        if inp[y][x] == '#':
            empty_column = False
            break
    if empty_column:
        empty_columns.add(x)

# Find the position of galaxies:
galaxies = set()
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == '#':
            galaxies.add((x, y))

solution = 0
for gal_a, gal_b in itertools.combinations(galaxies, 2):
    for x in empty_columns:
        if gal_a[0] < gal_b[0] and gal_a[0] < x < gal_b[0] \
                or gal_a[0] > gal_b[0] and gal_a[0] > x > gal_b[0]:
            solution += 1
    for y in empty_rows:
        if gal_a[1] < gal_b[1] and gal_a[1] < y < gal_b[1] \
                or gal_a[1] > gal_b[1] and gal_a[1] > y > gal_b[1]:
            solution += 1

    solution += abs(gal_a[0] - gal_b[0]) + abs(gal_a[1] - gal_b[1])

print(solution)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

# Expansion: get the index of empty lines and columns
empty_rows = set()
for y in range(len(inp)):
    if not '#' in inp[y]:
        empty_rows.add(y)

empty_columns = set()
for x in range(len(inp[0])):
    empty_column = True
    for y in range(len(inp)):
        if inp[y][x] == '#':
            empty_column = False
            break
    if empty_column:
        empty_columns.add(x)

# Find the position of galaxies:
galaxies = set()
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == '#':
            galaxies.add((x, y))

solution = 0
for gal_a, gal_b in itertools.combinations(galaxies, 2):
    empty_row_or_column_width = 1000000
    for x in empty_columns:
        if gal_a[0] < gal_b[0] and gal_a[0] < x < gal_b[0] \
                or gal_a[0] > gal_b[0] and gal_a[0] > x > gal_b[0]:
            solution += empty_row_or_column_width - 1
    for y in empty_rows:
        if gal_a[1] < gal_b[1] and gal_a[1] < y < gal_b[1] \
                or gal_a[1] > gal_b[1] and gal_a[1] > y > gal_b[1]:
            solution += empty_row_or_column_width - 1

    solution += abs(gal_a[0] - gal_b[0]) + abs(gal_a[1] - gal_b[1])

print(solution)

toc('Part 2 done in')
