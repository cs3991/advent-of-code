import itertools

from tictoc import tic, toc

with open("ex12.txt") as file:
    ex = [line.strip() for line in file if line.strip() != '']

with open("input12.txt") as file:
    inp = [line.strip() for line in file if line.strip() != '']

inp = ex

tic()
# -------- Part 1 -----------
print('   PART 1')


def generate_damaged_groups(condition_str):
    damaged_groups = []
    previous_char = '.'
    for c in condition_str:
        if c == '#':
            if previous_char == '.':
                damaged_groups.append(1)
            else:
                damaged_groups[-1] += 1
        previous_char = c
    return tuple(damaged_groups)


solution = 0

for line in inp:
    damaged_str, damaged_groups = line.split()
    damaged_groups = tuple(int(c) for c in damaged_groups.split(','))
    damaged_count = sum(damaged_groups)
    missing_damaged_count = damaged_count - damaged_str.count('#')
    unknown_count = damaged_str.count('?')
    for indexes in itertools.combinations(range(unknown_count), missing_damaged_count):
        result_list = []
        i = 0
        for c in damaged_str:
            if c != '?':
                result_list.append(c)
            else:
                if i in indexes:
                    result_list.append('#')
                else:
                    result_list.append('.')
                i += 1
        if generate_damaged_groups(''.join(result_list)) == damaged_groups:
            solution += 1

print(solution)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')


def generate_damaged_groups(condition_str):
    damaged_groups = []
    previous_char = '.'
    for c in condition_str:
        if c == '#':
            if previous_char == '.':
                damaged_groups.append(1)
            else:
                damaged_groups[-1] += 1
        previous_char = c
    return tuple(damaged_groups)


solution = 0

for line in inp:
    # print(line)
    damaged_str, damaged_groups = line.split()
    damaged_str: str = ((damaged_str + '?') * 5).removesuffix('?')
    damaged_groups = tuple(int(c) for c in damaged_groups.split(','))
    damaged_groups = damaged_groups * 5
    print(damaged_groups)
    damaged_count = sum(damaged_groups)
    missing_damaged_count = damaged_count - damaged_str.count('#')
    unknown_count = damaged_str.count('?')
    # for i in range(int(math.factorial(unknown_count) / (math.factorial(missing_damaged_count) * math.factorial(unknown_count - missing_damaged_count)))):
    for indexes in itertools.combinations(range(unknown_count), missing_damaged_count):
        result_list = []
        i = 0
        for c in damaged_str:
            if c != '?':
                result_list.append(c)
            else:
                if i in indexes:
                    result_list.append('#')
                else:
                    result_list.append('.')
                i += 1
        # print(''.join(result_list))
        # print(generate_damaged_groups(''.join(result_list)))
        # print(damaged_groups)
        if generate_damaged_groups(''.join(result_list)) == damaged_groups:
            # print('ok')
            solution += 1
    # print(solution)

print(solution)

toc('Part 2 done in')
