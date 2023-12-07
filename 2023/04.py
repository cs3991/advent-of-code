import re

from tictoc import tic, toc

with open("ex04.txt") as file:
    ex = [line.strip() for line in file if line.strip() != '']

with open("input04.txt") as file:
    inp = [line.strip() for line in file if line.strip() != '']
# inp = ex
# print(inp)

# -------- Part 1 -----------
print('   PART 1')
tic()
score = 0
for line in inp:
    matches = re.match(pattern=r'Card *[0-9]*: (.*) \| (.*)', string=line)
    winning = matches.group(1).split()
    numbers = matches.group(2).split()
    n_winning = 0
    for n in numbers:
        if n in winning:
            n_winning += 1
    if n_winning > 0:
        score += 2 ** (n_winning - 1)
toc('Part 1 done in')
print(score)
# -------- Part 2 -----------
print('   PART 2')
tic()
n_cards = 0
cards = []
cards_copies = dict()
for line in inp:
    matches = re.match(pattern=r'Card *([0-9]*): (.*) \| (.*)', string=line)
    id_card = int(matches.group(1))
    winning = matches.group(2).split()
    numbers = matches.group(3).split()
    cards.append((id_card, winning, numbers))
    cards_copies[id_card] = 1

for id_card, winning, numbers in cards:
    n_winning = 0
    for n in numbers:
        if n in winning:
            n_winning += 1
    for i in range(id_card + 1, n_winning + id_card + 1):
        cards_copies[i] += cards_copies[id_card]
    n_cards += cards_copies[id_card]

toc('Part 2 done in')
print(n_cards)

