import numpy as np
import sympy
from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter

with open("ex24.txt") as file:
    ex = [line.strip() for line in file if line.strip() != '']

with open("input24.txt") as file:
    inp = [line.strip() for line in file if line.strip() != '']
test_area = [200000000000000, 400000000000000]
# test_area = [7, 27]
# inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')
hailstones = []
for line in inp:
    pos_str, speed_str = line.split(' @ ')
    pos = tuple(int(i) for i in pos_str.split(', '))
    speed = tuple(int(i) for i in speed_str.split(', '))
    hailstones.append((pos, speed))
solution = 0
for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        pxa = hailstones[i][0][0]
        pya = hailstones[i][0][1]
        vxa = hailstones[i][1][0]
        vya = hailstones[i][1][1]
        pxb = hailstones[j][0][0]
        pyb = hailstones[j][0][1]
        vxb = hailstones[j][1][0]
        vyb = hailstones[j][1][1]
        slope_diff = vyb / vxb - vya / vxa
        if slope_diff != 0:
            x = 1 / slope_diff * (pya - pyb + vyb / vxb * pxb - vya / vxa * pxa)
            y = vya / vxa * (x - pxa) + pya
            if np.sign(x - pxa) == np.sign(vxa) and np.sign(x - pxb) == np.sign(vxb):
                if test_area[0] <= x <= test_area[1] and test_area[0] <= y <= test_area[1]:
                    solution += 1

print(solution)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
hailstones = []
for line in inp:
    pos_str, speed_str = line.split(' @ ')
    pos = tuple(int(i) for i in pos_str.split(', '))
    speed = tuple(int(i) for i in speed_str.split(', '))
    hailstones.append((pos, speed))
solution = 0

pxa = hailstones[0][0][0]
pya = hailstones[0][0][1]
pza = hailstones[0][0][2]
vxa = hailstones[0][1][0]
vya = hailstones[0][1][1]
vza = hailstones[0][1][2]
pxb = hailstones[1][0][0]
pyb = hailstones[1][0][1]
pzb = hailstones[1][0][2]
vxb = hailstones[1][1][0]
vyb = hailstones[1][1][1]
vzb = hailstones[1][1][2]
pxc = hailstones[2][0][0]
pyc = hailstones[2][0][1]
pzc = hailstones[2][0][2]
vxc = hailstones[2][1][0]
vyc = hailstones[2][1][1]
vzc = hailstones[2][1][2]

t1, t2, t3, px, vx, py, vy, pz, vz = sympy.symbols('t1 t2 t3 px vx py vy pz vz')
((t1, t2, t3, px, vx, py, vy, pz, vz),) = sympy.nonlinsolve([
    px + vx * t1 - (pxa + vxa * t1),
    py + vy * t1 - (pya + vya * t1),
    pz + vz * t1 - (pza + vza * t1),
    px + vx * t2 - (pxb + vxb * t2),
    py + vy * t2 - (pyb + vyb * t2),
    pz + vz * t2 - (pzb + vzb * t2),
    px + vx * t3 - (pxc + vxc * t3),
    py + vy * t3 - (pyc + vyc * t3),
    pz + vz * t3 - (pzc + vzc * t3),
], [t1, t2, t3, px, vx, py, vy, pz, vz])
print(px + py + pz)
toc('Part 2 done in')
