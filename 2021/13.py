from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input13.txt") as file:
    inp = [line.strip() for line in file]
coords = inp[:inp.index('')]
coords = [[int(n) for n in c.split(',')] for c in coords]

instr = [(0 if i[11] == 'x' else 1, int(i[13:])) for i in inp[inp.index('') + 1:]]

# print(coords)
print(instr)

# -------- Part 1 -----------
print('   PART 1')

i = instr[0][0]
fold = instr[0][1]
folded_coords = []
for n in range(len(coords)):
    new_coord = coords[n]
    if new_coord[i] > fold:
        new_coord[i] = 2 * fold - new_coord[i]
    if new_coord not in folded_coords:
        folded_coords.append(new_coord)
print(len(folded_coords))

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

def print2d(mat):
    for line in mat:
        for char in line:
            print(char, end='')
        print()

def build_mat(c):
    h = [e[0] for e in c]
    maxh = max(h)
    v = [e[1] for e in c]
    maxv = max(v)
    matrix = [[' ' for _i in range(maxv + 1)] for _j in range(maxh + 1)]
    for e in c:
        matrix[e[0]][e[1]] = '#'
    return matrix

def transpose(matrix):
    transpose = [[' ' for _i in range(len(matrix))] for _j in range(len(matrix[0]) + 1)]
    for l in range(len(matrix)):
        line = matrix[l]
        for c in range(len(line)):
            char = line[c]
            transpose[c][l] = matrix[l][c]
    return transpose

for instruction in instr:
    i = instruction[0]
    fold = instruction[1]
    folded_coords = []
    for n in range(len(coords)):
        new_coord = coords[n]
        if new_coord[i] > fold:
            new_coord[i] = 2 * fold - new_coord[i]
        if new_coord not in folded_coords:
            folded_coords.append(new_coord)
    coords = folded_coords

matrix = build_mat(coords)
print2d(transpose(matrix))

toc('Partie 2 terminée en')
