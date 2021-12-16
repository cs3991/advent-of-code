from tictoc import tic, toc

tic()

with open("input5.txt") as input_file:
    input_list = [[[int(n) for n in coords.split(',')]
                   for coords in line.split(' -> ')]
                  for line in input_file]
# print(input_list)

grid = {}

for segment in input_list:
    x0 = segment[0][0]
    y0 = segment[0][1]
    x1 = segment[1][0]
    y1 = segment[1][1]
    if x0 == x1:
        start = min(y0, y1)
        end = max(y0, y1)
        for i in range(start, end + 1):
            if (x0, i) in grid:
                grid[(x0, i)] += 1
            else:
                grid[(x0, i)] = 1
    elif y0 == y1:
        start = min(x0, x1)
        end = max(x0, x1)
        for i in range(start, end + 1):
            if (i, y0) in grid:
                grid[(i, y0)] += 1
            else:
                grid[(i, y0)] = 1
    else:  # ----------- Part 2 ----------------------
        startx = min(x0, x1)
        endx = max(x0, x1)
        length = endx - startx
        if x1 - x0 > 0:
            directionx = 1
        else:
            directionx = -1
        if y1 - y0 > 0:
            directiony = 1
        else:
            directiony = -1
        for i in range(length + 1):
            if (x0 + directionx * i, y0 + directiony * i) in grid:
                grid[(x0 + directionx * i, y0 + directiony * i)] += 1
            else:
                grid[(x0 + directionx * i, y0 + directiony * i)] = 1
    # ------------------------------------------------

sum_overlap = 0
for element in grid:
    if grid[element] >= 2:
        sum_overlap += 1
print(sum_overlap)

toc()

# ----------------------------- Justin ------------------------------------------------------

import numpy as np

grille = np.zeros((1000, 1000))
number = 0
# --------part 1----------------------
for i in range(len(input_list)):
    x1 = input_list[i][0][0]
    x2 = input_list[i][1][0]
    y1 = input_list[i][0][1]
    y2 = input_list[i][1][1]

    if x1 == x2:
        if y1 < y2:
            grille[x1, y1:y2 + 1] += 1
        else:
            grille[x1, y2:y1 + 1] += 1

    elif y1 == y2:
        if x1 < x2:
            grille[x1:x2 + 1, y1] += 1
        else:
            grille[x2:x1 + 1, y1] += 1

    # --------part 2----------------------
    elif x1 != x2 and y1 != y2:
        length = abs(x1 - x2)
        if x2 - x1 > 0:
            directionx = 1
        else:
            directionx = -1
        if y2 - y1 > 0:
            directiony = 1
        else:
            directiony = -1
        for i in range(length + 1):
            if (x1 + directionx * i, y1 + directiony * i) in grid:
                grille[(x1 + directionx * i, y1 + directiony * i)] += 1
            else:
                grille[(x1 + directionx * i, y1 + directiony * i)] = 1

    # elif x1 != x2 and y1 != y2:
    #     if x1 < x2 and y1 < y2:
    #         for j in range(abs(x2 - x1) + 1):
    #             grille[x1 + j, y1 + j] += 1
    #     elif x1 > x2 and y1 > y2:
    #         for j in range(abs(x2 - x1) + 1):
    #             grille[x2 + j, y2 + j] += 1
    #     elif x1 > x2 and y1 < y2:
    #         for j in range(abs(x2 - x1) + 1):
    #             grille[x2 + j, y2 - j] += 1
    #     elif x1 < x2 and y1 > y2:
    #         for j in range(abs(x2 - x1) + 1):
    #             grille[x1 + j, y1 - j] += 1

# ---------------------------------------

count = 0
for i in range(len(grille)):
    for j in range(len(grille[0])):
        if grille[i, j] >= 2:
            count += 1
print(count)
toc()