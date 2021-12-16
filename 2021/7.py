from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input7.txt") as input_file:
    input_list = [int(n) for n in input_file.readline().split(',')]
# print(input_list)

# -------- Part 1 -----------
print('   PART 1')

fuel2 = None
for i in range(max(input_list)):
    fuel = 0
    for crab in input_list:
        fuel += abs(crab - i)
    # print(i, fuel)
    if i != 0 and fuel2 < fuel:
        print('solution :', i - 1, ', fuel :', fuel2)
        break
    fuel2 = fuel

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

fuel2 = None
for i in range(max(input_list)):
    fuel = 0
    for crab in input_list:
        fuel += (abs(crab - i) + 1) * (abs(crab - i) + 2) / 2
        # print(i, fuel)
    if i != 0 and fuel2 < fuel:
        print('solution :', i - 1, ', fuel :', fuel2)
        break
    fuel2 = fuel

toc('Partie 2 terminée en')
