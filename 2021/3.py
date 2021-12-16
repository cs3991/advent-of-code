from tictoc import tic, toc
from numpy import where

tic()

with open("input3.txt") as input_file:
    input_list = [line.replace('\n', '') for line in input_file]

# -------- Part 1 -----------
epsilon = ''
gamma = ''
n = len(input_list)
for i in range(len(input_list[0])):
    ones_counter = 0
    for number in input_list:
        if number[i] == '1':
            ones_counter += 1
    if ones_counter > n / 2:
        epsilon += '1'
        gamma += '0'
    else:
        epsilon += '0'
        gamma += '1'
print('epsilon =', epsilon)
print(int(epsilon, 2))
print('gamma =', gamma)
print(int(gamma, 2))

result = int(epsilon, 2) * int(gamma, 2)

print('result = ', result)

# -------- Part 2 -----------
co2_list = input_list.copy()
o2_list = input_list.copy()
for bit in range(len(input_list[0])):
    ones_counter = 0
    for number in co2_list:
        if number[bit] == '1':
            ones_counter += 1
    if ones_counter >= len(co2_list) / 2:
        bit_criteria = '1'
    else:
        bit_criteria = '0'
    for number in co2_list.copy():
        if number[bit] != bit_criteria:
            co2_list.remove(number)
        if len(co2_list) == 1:
            co2 = int(co2_list[0], 2)
            print(co2_list[0], co2)
            break
for bit in range(len(input_list[0])):
    ones_counter = 0
    for number in o2_list:
        if number[bit] == '1':
            ones_counter += 1
    if ones_counter >= len(o2_list) / 2:
        bit_criteria = '0'
    else:
        bit_criteria = '1'
    for number in o2_list.copy():
        if number[bit] != bit_criteria:
            o2_list.remove(number)
        if len(o2_list) == 1:
            o2 = int(o2_list[0], 2)
            print(o2_list[0], o2)
            break
print(o2 * co2)

toc()

input_binary = [int(n, 2) for n in input_list]

# -------- Part 1 -----------
epsilon = 0
for bit in range(len(input_list[0])):
    mask = 2 ** (len(input_list[0]) - 1 - bit)
    average = 0
    for number in input_binary:
        average += mask & number
    average /= len(input_binary)
    if average >= mask / 2:
        epsilon += mask
print(epsilon)
gamma = epsilon ^ 2 ** (len(input_list[0])) - 1
print(gamma)
print(gamma * epsilon)
# -------- Part 2 -----------

toc()
