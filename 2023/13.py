from tictoc import tic, toc

with open("ex13.txt") as file:
    ex = file.read()

with open("input13.txt") as file:
    inp = file.read()

tic()
# -------- Part 1 -----------
print('   PART 1')
patterns = []
for pattern in inp.strip().split('\n\n'):
    lines = []
    for line in pattern.splitlines():
        lines.append(tuple(line))
    patterns.append(tuple(lines))
patterns = tuple(patterns)


def check_v_axis(line, axis_index):
    number_modifications = 0
    for n in range(min(len(line) - axis_index, axis_index)):
        assert axis_index - 1 - n >= 0
        assert axis_index + n >= 0
        left_element = line[axis_index - 1 - n]
        right_element = line[axis_index + n]
        if left_element != right_element:
            number_modifications += 1
    return number_modifications


solution = 0
# find vertical axis of symmetry
for pattern in patterns:
    found_axis = False
    possible_axis = set(range(1, len(pattern[0])))
    next_possible_axis = possible_axis.copy()
    for y in range(len(pattern)):
        line = pattern[y]
        for axis_index in possible_axis:
            if not check_v_axis(line, axis_index) == 0:
                next_possible_axis.discard(axis_index)
            possible_axis = next_possible_axis.copy()
    if len(possible_axis) == 1:
        found_axis = True
        (axis,) = possible_axis
        solution += axis
        continue

    # find horizontal axis of symmetry
    possible_axis = set(range(1, len(pattern)))
    next_possible_axis = possible_axis.copy()
    for x in range(len(pattern[0])):
        column = [line[x] for line in pattern]
        for axis_index in possible_axis:
            if not check_v_axis(column, axis_index) == 0:
                next_possible_axis.discard(axis_index)
            possible_axis = next_possible_axis.copy()
    if len(possible_axis) == 1:
        found_axis = True
        (axis,) = possible_axis
        solution += 100 * axis
        continue
    assert found_axis
print(solution)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

solution = 0
# find vertical axis of symmetry
for pattern in patterns:
    found_axis = False
    possible_axis = set(range(1, len(pattern[0])))
    possible_axis_with_1_modif = set()
    next_possible_axis = possible_axis.copy()
    next_possible_axis_with_1_modif = possible_axis_with_1_modif.copy()
    for y in range(len(pattern)):
        line = pattern[y]
        for axis_index in possible_axis.union(possible_axis_with_1_modif):
            number_modifications = check_v_axis(line, axis_index)
            if number_modifications == 1:
                if axis_index in next_possible_axis:
                    next_possible_axis.discard(axis_index)
                    next_possible_axis_with_1_modif.add(axis_index)
                else:
                    next_possible_axis_with_1_modif.discard(axis_index)
            elif number_modifications != 0:
                next_possible_axis.discard(axis_index)
                next_possible_axis_with_1_modif.discard(axis_index)
            possible_axis = next_possible_axis.copy()
            possible_axis_with_1_modif = next_possible_axis_with_1_modif.copy()
    if len(possible_axis_with_1_modif) == 1:
        found_axis = True
        (axis,) = possible_axis_with_1_modif
        solution += axis
        continue

    # find horizontal axis of symmetry
    possible_axis = set(range(1, len(pattern)))
    possible_axis_with_1_modif = set()
    next_possible_axis = possible_axis.copy()
    next_possible_axis_with_1_modif = possible_axis_with_1_modif.copy()
    for x in range(len(pattern[0])):
        column = [line[x] for line in pattern]
        for axis_index in possible_axis.union(possible_axis_with_1_modif):
            number_modifications = check_v_axis(column, axis_index)
            if number_modifications == 1:
                if axis_index in next_possible_axis:
                    next_possible_axis.discard(axis_index)
                    next_possible_axis_with_1_modif.add(axis_index)
                else:
                    next_possible_axis_with_1_modif.discard(axis_index)
            elif number_modifications != 0:
                next_possible_axis.discard(axis_index)
                next_possible_axis_with_1_modif.discard(axis_index)
            possible_axis = next_possible_axis.copy()
            possible_axis_with_1_modif = next_possible_axis_with_1_modif.copy()

    if len(possible_axis_with_1_modif) == 1:
        found_axis = True
        (axis,) = possible_axis_with_1_modif
        solution += 100 * axis
        continue
    assert found_axis
print(solution)

toc('Part 2 done in')
