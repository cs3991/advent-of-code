from tictoc import tic, toc

tic()

with open("input4.txt") as input_file:
    input_numbers = [int(n) for n in input_file.readline().split(',')]
    input_file.readline()
    input_grids = [grid.splitlines() for grid in input_file.read().split('\n\n')]
    input_grids = [[[int(n) for n in line.split()] for line in grid] for grid in input_grids]



# -------- Fonctions générales -----------
def check_for_win(grid, i, j):
    # pour la ligne
    winning_line = True
    for number in grid[i]:
        if number != '':
            winning_line = False
    # pour la colonne
    winning_column = True
    column = [line[j] for line in grid]
    for number in column:
        if number != '':
            winning_column = False
    return winning_line or winning_column

def total_sum(grid):
    sum = 0
    for line in grid:
        for element in line:
            if element != '':
                sum += element
    return sum

# -------- Part 1 -----------
print('PART 1')

def part1():
    for draw in input_numbers:
        for grid in input_grids:
            for line in grid:
                for number in line:
                    if number == draw:
                        i = grid.index(line)
                        j = line.index(number)
                        line[j] = ''
                        if check_for_win(grid, i, j):
                            print(total_sum(grid) * draw)
                            return

# part1()

# -------- Part 2 -----------
print('PART 2')

def part2():
    grid_index_won = []
    for draw in input_numbers:
        for grid in input_grids:
            if input_grids.index(grid) not in grid_index_won:
                for line in grid:
                    for number in line:
                        if number == draw:
                            i = grid.index(line)
                            j = line.index(number)
                            line[j] = ''
                            if check_for_win(grid, i, j):
                                grid_index_won.append(input_grids.index(grid))
                                if len(input_grids) == len(grid_index_won):
                                    print(total_sum(grid) * draw)
                                    return
part2()

toc()