from tictoc import tic, toc

with open("ex14.txt") as file:
    ex = tuple(tuple(line.strip()) for line in file if line.strip() != '')

with open("input14.txt") as file:
    inp = tuple(tuple(line.strip()) for line in file if line.strip() != '')
# inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')
solution = 0
inp_after_tilt = [list(l) for l in inp]
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp_after_tilt[y][x] == 'O':
            dy = 1
            while y - dy >= 0 and inp_after_tilt[y - dy][x] == '.':
                dy += 1
            inp_after_tilt[y][x] = '.'
            inp_after_tilt[y - dy + 1][x] = 'O'
            solution += len(inp) - (y - dy + 1)

print(solution)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
solution = 0
inp_after_tilt = [list(l) for l in inp]


def tilt_north():
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp_after_tilt[y][x] == 'O':
                dy = 1
                while y - dy >= 0 and inp_after_tilt[y - dy][x] == '.':
                    dy += 1
                inp_after_tilt[y][x] = '.'
                inp_after_tilt[y - dy + 1][x] = 'O'


def tilt_south():
    for y in range(len(inp) - 1, -1, -1):
        for x in range(len(inp[0])):
            if inp_after_tilt[y][x] == 'O':
                dy = 1
                while y + dy < len(inp) and inp_after_tilt[y + dy][x] == '.':
                    dy += 1
                inp_after_tilt[y][x] = '.'
                inp_after_tilt[y + dy - 1][x] = 'O'


def tilt_east():
    for y in range(len(inp)):
        for x in range(len(inp[0]) - 1, -1, -1):
            if inp_after_tilt[y][x] == 'O':
                dx = 1
                while x + dx < len(inp[0]) and inp_after_tilt[y][x + dx] == '.':
                    dx += 1
                inp_after_tilt[y][x] = '.'
                inp_after_tilt[y][x + dx - 1] = 'O'


def tilt_west():
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp_after_tilt[y][x] == 'O':
                dx = 1
                while x - dx >= 0 and inp_after_tilt[y][x - dx] == '.':
                    dx += 1
                inp_after_tilt[y][x] = '.'
                inp_after_tilt[y][x - dx + 1] = 'O'


positions = {}
number_of_steps = 1_000_000_000
least_equivalent_step = None
for step_count in range(1, number_of_steps + 1):
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()
    key = tuple(tuple(l) for l in inp_after_tilt)
    if key in positions.keys():
        if least_equivalent_step == step_count:
            break
        if least_equivalent_step is None:
            cycle_length = step_count - positions[key]
            remaining_steps = number_of_steps - step_count
            least_equivalent_step = remaining_steps % cycle_length + step_count
    positions[key] = step_count

for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp_after_tilt[y][x] == 'O':
            solution += len(inp) - y
print(solution)

toc('Part 2 done in')
