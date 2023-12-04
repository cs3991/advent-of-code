import itertools

from tictoc import tic, toc

with open("ex03.txt") as file:
    ex = [[c for c in line.strip()] for line in file]

with open("input03.txt") as file:
    inp = [[c for c in line.strip()] for line in file]
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')
# inp = ex
directions = set(itertools.product([-1, 0, 1], repeat=2))
solution = 0
part_numbers = []
current_number_str = ''
part_number = False
# Iteration sur les cases du tableau
for y in range(len(inp)):
    for x in range(len(inp[y])):
        char = inp[y][x]
        # Si le caractère courant est un chiffre
        if char.isdigit():
            # on va completer le nombre en cours
            current_number_str += char
            for dx, dy in directions:
                # est ce qu'on sort de la grille ?
                if 0 <= x + dx < len(inp[y]) and 0 <= y + dy < len(inp):
                    # si un caractère adjacent n'est ni un . ni un chiffre
                    if not inp[y + dy][x + dx].isdigit() and not inp[y + dy][x + dx] == '.':
                        # alors c'est un part number
                        part_number = True
        # Si c'est la fin du nombre
        if current_number_str != '' and (x + 1 >= len(inp[y]) or not inp[y][x + 1].isdigit()):
            if part_number:
                part_numbers.append(int(current_number_str))
                solution += int(current_number_str)
            current_number_str = ''
            part_number = False
print(solution)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

toc('Part 2 done in')
