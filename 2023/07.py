from collections import defaultdict
from functools import cmp_to_key

from tictoc import tic, toc

with open("ex07.txt") as file:
    ex = [line.strip().split() for line in file if line.strip() != '']

with open("input07.txt") as file:
    inp = [line.strip().split() for line in file if line.strip() != '']

# inp = ex
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')
strengths = []
plays = [e.copy() for e in inp]
for play in plays:
    hand, bid = play[0], play[1]
    char_count = defaultdict(int)
    for char in hand:
        char_count[char] += 1
    count_list = list(char_count.values())
    count_list.sort(reverse=True)
    if count_list[0] == 5:
        strength = 7
    elif count_list[0] == 4:
        strength = 6
    elif count_list == [3, 2]:
        strength = 5
    elif count_list[0] == 3:
        strength = 4
    elif count_list[0] == 2 and count_list[1] == 2:
        strength = 3
    elif count_list[0] == 2:
        strength = 2
    else:
        strength = 1
    play.append(strength)


def compare(play_a, play_b):
    cards_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if play_a[2] > play_b[2]:
        return 1
    if play_a[2] < play_b[2]:
        return -1
    for i in range(5):
        if play_a[0][i] != play_b[0][i]:
            return cards_order.index(play_b[0][i]) - cards_order.index(play_a[0][i])


plays.sort(key=cmp_to_key(compare), reverse=False)
solution = 0
for i, item in enumerate(plays):
    solution += int(item[1]) * (i + 1)

print(solution)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

cards_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

strengths = []
plays = [e.copy() for e in inp]
for play in plays:
    hand, bid = play[0], play[1]
    char_count = defaultdict(int)
    for char in hand:
        char_count[char] += 1
    number_of_jokers = char_count['J']
    del char_count['J']
    count_list = list(char_count.values())
    count_list.sort(reverse=True)
    if count_list == []:
        count_list = [0]
    if count_list[0] == 5 - number_of_jokers:
        strength = 7
    elif count_list[0] == 4 - number_of_jokers:
        strength = 6
    elif count_list == [3, 2] or (count_list == [2, 2] and number_of_jokers == 1):
        strength = 5
    elif count_list[0] == 3 - number_of_jokers:
        strength = 4
    elif count_list[0] == 2 and count_list[1] == 2:
        strength = 3
    elif count_list[0] == 2 - number_of_jokers:
        strength = 2
    else:
        strength = 1
    play.append(strength)


def compare(play_a, play_b):
    if play_a[2] > play_b[2]:
        return 1
    if play_a[2] < play_b[2]:
        return -1
    for i in range(5):
        if play_a[0][i] != play_b[0][i]:
            return cards_order.index(play_b[0][i]) - cards_order.index(play_a[0][i])


plays.sort(key=cmp_to_key(compare), reverse=False)
solution = 0
for i, item in enumerate(plays):
    solution += int(item[1]) * (i + 1)

print(solution)

toc('Part 2 done in')
