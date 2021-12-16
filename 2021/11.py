from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input11.txt") as file:
    inp = [[int(n) for n in line.strip()] for line in file]
# print(inp)

# -------- Part 1 et 2 -----------
print('   PART 1 et 2')

flashes = 0
hdir = [0, 1, 1, 1, 0, -1, -1, -1]
vdir = [1, 1, 0, -1, -1, -1, 0, 1]
stop = False
itern = 1
while not stop:
    queue = []
    flashed = set()
    # increment all octopus:
    for l in range(len(inp)):
        for c in range(len(inp[l])):
            inp[l][c] += 1
    # print_inp(inp)
    # flash all > 9, increment all adjacents
    continue_step = True
    while continue_step:
        continue_step = False
        to_incr = []
        for l in range(len(inp)):
            for c in range(len(inp[l])):
                if inp[l][c] > 9 and (l, c) not in flashed:
                    continue_step = True
                    flashes += 1
                    flashed.add((l, c ))
                    for n in range(8):
                        if 0 <= l + vdir[n] < len(inp) and 0 <= c + hdir[n] < len(inp[l]):
                            to_incr.append((l + vdir[n], c + hdir[n]))
        for coord in to_incr:
            inp[coord[0]][coord[1]] += 1
    # set to 0 all flashed
    for coord in flashed:
        inp[coord[0]][coord[1]] = 0
    if len(flashed) == len(inp) * len(inp[0]):
        stop = True
        print(itern)
    if itern == 100:
        print('à l\'itération 100 : nombre de flash :', flashes)
    itern += 1
toc('Terminée en')
