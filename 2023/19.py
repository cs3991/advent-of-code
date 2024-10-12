from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter


with open("ex19.txt") as file:
    ex = file.read()

with open("input19.txt") as file:
    inp = file.read()

inp = ex

tic()
# -------- Part 1 -----------
print('   PART 1')
workflow_str, pieces_str = inp.split('\n\n')
print(workflow_str, pieces_str)


toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')


toc('Part 2 done in')