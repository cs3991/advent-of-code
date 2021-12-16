from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input10.txt") as input_file:
    input_list = [line for line in input_file]
# print(input_list)

# -------- Part 1 -----------
print('   PART 1')
point = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
op = ['(', '[', '{', '<']
cl = [')', ']', '}', '>']
matching = dict(zip(cl, op))
score = 0
for line in input_list:
    opened = []
    for char in line:
        if char in op:
            opened.append(char)
        if char in cl:
            if opened[-1] != matching[char]:
                score += point[char]
                break
            else:
                del opened[-1]
print(score)
toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

point = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

score = []
for line in input_list:
    opened = []
    for i in range(len(line)):
        char = line[i]
        lscore = 0
        if char in op:
            opened.append(char)
        if char in cl:
            if opened[-1] != matching[char]:
                break
            else:
                del opened[-1]
        if i == len(line) - 1:
            if opened:
                opened.reverse()
                for left_opened in opened:
                    lscore *= 5
                    lscore += point[left_opened]
            score.append(lscore)
        i += 1
score.sort()
print(score[len(score) // 2])
toc('Partie 2 terminée en')
