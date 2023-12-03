from tictoc import tic, toc

with open("ex2.txt") as file:
    ex = [line.strip() for line in file]

with open("input2.txt") as file:
    inp = [line.strip() for line in file]
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')

initial_bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

parsed = []
for game in inp:
    game = game.split(': ')
    game_id = int(game[0].replace('Game ', ''))
    game_list = []
    for show in game[1].split('; '):
        draw_dic = dict()
        for color in show.split(', '):
            draw_dic[color.split(' ')[1]] = int(color.split(' ')[0])
        game_list.append(draw_dic)
    parsed.append(game_list)

solution = 0
for i, game in enumerate(parsed):
    possible = 1
    for show in game:
        for color in show:
            if show[color] > initial_bag[color]:
                possible = 0
                break
    if possible == 1:
        solution += i + 1
print(solution)

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')
solution = 0
for i, game in enumerate(parsed):
    number_of_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for show in game:
        for color in show:
            if show[color] > number_of_cubes[color]:
                number_of_cubes[color] = show[color]
    solution += (number_of_cubes['red']
                 * number_of_cubes['green']
                 * number_of_cubes['blue'])
print(solution)
toc('Partie 2 terminée en')
