from tictoc import tic, toc

tic()

with open("input1.txt") as input_file:
    input_list = [int(n) for n in input_file]

# -------- Part 1 -----------
result1 = 0
for i in range(1, len(input_list)):
    if input_list[i] > input_list[i - 1]:
        result1 += 1

print(result1)

# -------- Part 2 -----------
result2 = 0
previous_sum = 0
for i in range(2, len(input_list)):
    current_sum = 0
    for j in range(3):
        current_sum += input_list[i - j]
    if i != 3:
        if current_sum > previous_sum:
            result2 += 1
    previous_sum = current_sum
print(result2)

toc()
