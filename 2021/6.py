from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input6.txt") as input_file:
    input_list = [int(n) for n in input_file.readline().split(',')]
# print(input_list)
input_list2 = input_list.copy()
# -------- Part 1 -----------

print('   PART 1')
for day in range(80):
    fishes_to_add = []
    for i in range(len(input_list)):
        if input_list[i] == 0:
            input_list[i] = 6
            fishes_to_add.append(8)
        else:
            input_list[i] -= 1
    input_list.extend(fishes_to_add)
print(len(input_list))

toc('Part 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

number_of_fishes = Counter(input_list2)

for day in range(256):
    new_number_of_fishes = defaultdict(int)
    for fish in number_of_fishes:
        if fish == 0:
            new_number_of_fishes[6] += number_of_fishes[fish]
            new_number_of_fishes[8] += number_of_fishes[fish]
        else:
            new_number_of_fishes[fish - 1] += number_of_fishes[fish]
    number_of_fishes = new_number_of_fishes
count = 0

print(sum(number_of_fishes.values()))

toc('Part 2 terminée en')
