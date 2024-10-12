from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter

with open("ex18.txt") as file:
    ex = [line.strip() for line in file if line.strip() != '']

with open("input18.txt") as file:
    inp = [line.strip() for line in file if line.strip() != '']
inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')
dir_dict = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
border = set()
current_tile = (0, 0)
for line in inp:
    dir_str, l_str, color_str = line.split(' ')
    dir = dir_dict[dir_str]
    l = int(l_str)
    for _ in range(l):
        current_tile = (current_tile[0] + dir[1], current_tile[1] + dir[0])
        border.add(current_tile)

max_x, max_y = 0, 0
min_x, min_y = 0, 0
for x, y in border:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y

solution = len(border)

# ensure the current tile is in the pool:
current_tile = (max_x, max_y)
while current_tile not in border:
    current_tile = (current_tile[0] - 1, current_tile[1] - 1)
current_tile = (current_tile[0] - 1, current_tile[1] - 1)

# add the interior to the solution:
tiles = [current_tile]
explored = set()
while len(tiles) != 0:
    next_tiles = []
    for tile in tiles:
        for dir in dir_dict.values():
            explored_tile = (tile[0] + dir[0], tile[1] + dir[1])
            if explored_tile not in explored and explored_tile not in border:
                explored.add(explored_tile)
                next_tiles.append(explored_tile)
                solution += 1
    tiles = next_tiles.copy()

print(solution)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
dir_dict = {'3': (-1, 0), '1': (1, 0), '0': (0, 1), '2': (0, -1)}

border = set()
current_tile = (0, 0)
for line in inp:
    _, _, color_str = line.split(' ')
    dir = dir_dict[color_str[7]]
    l = int(color_str[2:7], base=16)
    for _ in range(l):
        current_tile = (current_tile[0] + dir[1], current_tile[1] + dir[0])
        border.add(current_tile)

max_x, max_y = 0, 0
min_x, min_y = 0, 0
for x, y in border:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y

solution = len(border)
print(len(border))

# ensure the current tile is in the pool:
current_tile = (max_x, max_y)
while current_tile not in border:
    current_tile = (current_tile[0] - 1, current_tile[1] - 1)
current_tile = (current_tile[0] - 1, current_tile[1] - 1)

# print(current_tile)
# for y in range(min_y, max_y + 1):
#     for x in range(min_x, max_x + 1):
#         if (x, y) == current_tile:
#             print('o', end='')
#         elif (x, y) in border:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()


# add the interior to the solution:
tiles = [current_tile]
explored = set()
while len(tiles) != 0:
    next_tiles = []
    for tile in tiles:
        for dir in dir_dict.values():
            explored_tile = (tile[0] + dir[0], tile[1] + dir[1])
            if explored_tile not in explored and explored_tile not in border:
                explored.add(explored_tile)
                next_tiles.append(explored_tile)
                solution += 1
    tiles = next_tiles.copy()
    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         if (x, y) in next_tiles:
    #             print('+', end='')
    #         elif (x, y) in explored:
    #             print('o', end='')
    #         elif (x, y) in border:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()

print(solution)
toc('Part 2 done in')
