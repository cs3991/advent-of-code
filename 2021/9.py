from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input9.txt") as input_file:
    m = [[int(n) for n in list(line.strip())] for line in input_file]
# print(m)

# -------- Part 1 -----------
print('   PART 1')
count = 0
for l in range(len(m)):
    for c in range(len(m[l])):
        up, down, left, right = 10, 10, 10, 10
        if l > 0:
            up = m[l - 1][c]
        if l < len(m) - 1:
            down = m[l + 1][c]
        if c > 0:
            left = m[l][c - 1]
        if c < len(m[l]) - 1:
            right = m[l][c + 1]
        if m[l][c] < min([up, down, left, right]):
            count += m[l][c] + 1
print(count)
toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')


def find_bassin(m, l, c):
    s = set()
    if l > 0:
        up = m[l - 1][c]
        if up > m[l][c] and up != 9:
            s = s.union(find_bassin(m, l - 1, c))
    if l < len(m) - 1:
        down = m[l + 1][c]
        if down > m[l][c] and down != 9:
            s = s.union(find_bassin(m, l + 1, c))
    if c > 0:
        left = m[l][c - 1]
        if left > m[l][c] and left != 9:
            s = s.union(find_bassin(m, l, c - 1))
    if c < len(m[l]) - 1:
        right = m[l][c + 1]
        if right > m[l][c] and right != 9:
            s = s.union(find_bassin(m, l, c + 1))
    s.add((l, c))
    return s

sizesm = 1
bassins = []
for l in range(len(m)):
    for c in range(len(m[l])):
        up, down, left, right = 10, 10, 10, 10
        if l > 0:
            up = m[l - 1][c]
        if l < len(m) - 1:
            down = m[l + 1][c]
        if c > 0:
            left = m[l][c - 1]
        if c < len(m[l]) - 1:
            right = m[l][c + 1]
        if m[l][c] < min([up, down, left, right]):
            bassins.append(len(find_bassin(m, l, c)))
for size in sorted(bassins, reverse=True)[0:3]:
    sizesm *= size
print(sizesm)

toc('Partie 2 terminée en')