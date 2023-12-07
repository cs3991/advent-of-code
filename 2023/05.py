from tictoc import tic, toc

with open(r"ex05.txt") as file:
    ex = file.read().strip()

with open(r"input05.txt") as file:
    inp = file.read().strip()
# inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')
mapping_functions = inp.split('\n\n')
for i in range(len(mapping_functions)):
    if i == 0:

        mapping_functions[i] = [int(s) for s in mapping_functions[i].replace('seeds: ', '').split(' ')]
    else:
        mapping_functions[i] = [[int(s) for s in line_part.split(' ')] for line_part in
                                mapping_functions[i].strip().split('\n')[1:]]

seeds_list = mapping_functions[0]
del mapping_functions[0]

location_list = []
for seed in seeds_list:
    item = seed
    for map in mapping_functions:
        for line in map:
            source = line[1]
            dest = line[0]
            length = line[2]
            if source <= item <= source + length:
                item = item - source + dest
                break
    location_list.append(item)
print(min(location_list))
toc('Part 1 done in')

# -------- Part 2 -----------
print('   PART 2')
mapping_functions = inp.split('\n\n')
for i in range(len(mapping_functions)):
    if i == 0:

        mapping_functions[i] = [int(s) for s in mapping_functions[i].replace('seeds: ', '').split(' ')]
    else:
        mapping_functions[i] = [[int(s) for s in line_part.split(' ')] for line_part in
                                mapping_functions[i].strip().split('\n')[1:]]

range_list = mapping_functions[0]
del mapping_functions[0]
range_list = [(range_list[i], range_list[i + 1]) for i in range(0, len(range_list), 2)]

solution = 0
found_solution = False
mapping_functions.reverse()
while not found_solution:
    seed_number = solution
    for mapping_function in mapping_functions:
        for map_line in mapping_function:
            if map_line[0] <= seed_number < map_line[0] + map_line[2]:
                seed_number = seed_number - map_line[0] + map_line[1]
                break
    for seed in range_list:
        if seed[0] <= seed_number < seed[0] + seed[1]:
            found_solution = True
            print(solution)
    solution += 1
toc('Part 2 done in')
