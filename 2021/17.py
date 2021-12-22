from cprint import cprint
from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

targetx = (185, 221)
targety = (-122, -74)

ex1_targetx = (20, 30)
ex1_targety = (-10, -5)
expected1 = 45
# print(inp)

# -------- Part 1 -----------
cprint('   PART 1', 'blue', bold=True)

def launch(vx, vy, targetx, targety):
    """
    Simule un lancement avec comme vitesse initiale vx, vy et renvoie si la cible est atteinte avec ce lancé
    """
    x = 0
    y = 0
    while True:
        x += vx
        y += vy
        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        if targetx[0] <= x <= targetx[1] and targety[0] <= y <= targety[1]:
            return True
        elif y < targety[0] or x > targetx[1]:
            return False


def launchy(vy, targety):
    """
    Simule un lancement en tenant compte seulement du y. Renvoie la hauteur max du lancé
    """
    max_height = 0
    y = 0
    while True:
        y += vy
        vy -= 1
        if y > max_height:
            max_height = y
        if targety[0] <= y <= targety[1]:
            return max_height
        elif y < targety[0]:
            return None


def part1(targety):
    # On peut raisonner uniquement sur les y puisqu'on peut trouver un x qui touche la cible pour tout y
    max_height = 0
    ymax = - (targety[0] - 1)
    for y in range(targety[0], ymax + 1):
        height = launchy(y, targety)
        if height is not None and height > max_height:
            max_height = height
    return max_height

solution_1_ex = part1(ex1_targety)
if solution_1_ex == expected1:
    cprint('Test sur l\'exemple OK', 'green', bold=True)
else:
    cprint(f'Test échoué : valeur trouvé : {solution_1_ex}, valeur attendue : {expected1}', 'red', bold=True)

print(part1(targety))

toc('Partie 1 terminée en')
# -------- Part 2 -----------
cprint('   PART 2', 'blue', bold=True)


def part2(targetx, targety):
    count = 0
    ymax = - (targety[0] - 1)
    for x in range(targetx[1] + 1):
        for y in range(targety[0], ymax + 1):
            touched = launch(x, y, targetx, targety)
            if touched:
                count += 1
    return count

expected2 = 112

solution_2_ex = part2(ex1_targetx, ex1_targety)
if solution_2_ex == expected2:
    cprint('Test sur l\'exemple OK', 'green', bold=True)
else:
    cprint(f'Test échoué : valeur trouvé : {solution_2_ex}, valeur attendue : {expected2}', 'red', bold=True)

print(part2(targetx, targety))


toc('Partie 2 terminée en')