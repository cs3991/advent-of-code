import numpy as np

from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter

with open("ex17.txt") as file:
    ex = tuple(tuple(int(c) for c in line.strip()) for line in file if line.strip() != '')

with open("input17.txt") as file:
    inp = tuple(tuple(int(c) for c in line.strip()) for line in file if line.strip() != '')
# inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')

start = (0, (0, 0), (0, 0), {(0, 0)})
paths = [start]
visited = {(0, 0, 0, 0)}  # i, j, i_rect, j_rect
directions = {
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
}

while paths[0][1] != (len(inp) - 1, len(inp[0]) - 1):
    current_path = paths[0]
    reverse_dir = (-np.sign(current_path[2][0]), -np.sign(current_path[2][1]))
    for di, dj in directions.difference({reverse_dir}):
        i = current_path[1][0]
        j = current_path[1][1]
        if 0 <= i + di < len(inp) and 0 <= j + dj < len(inp[0]):
            i_rect = current_path[2][0]
            j_rect = current_path[2][1]
            if (di == 0 and i_rect == 0) or (dj == 0 and j_rect == 0):
                rect_move = (di + i_rect, dj + j_rect)
            else:
                rect_move = (di, dj)
            if (i + di, j + dj, rect_move[0], rect_move[1]) not in visited:
                if max(abs(i_rect + di), abs(j_rect + dj)) <= 3:
                    paths.append((current_path[0] + inp[i + di][j + dj], (i + di, j + dj), rect_move))
                    visited.add((i + di, j + dj, rect_move[0], rect_move[1]))
    paths.remove(current_path)
    paths.sort(key=lambda path: path[0])

print(paths[0][0])

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

toc('Part 2 done in')
