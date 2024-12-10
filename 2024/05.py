from tictoc import tic, toc


def parse(file):
    rules, updates = file.read().strip().split('\n\n')
    rules = [tuple(int(s) for s in pages.split('|')) for pages in rules.split('\n')]
    updates = [[int(s) for s in pages.split(',')] for pages in updates.split('\n')]
    return rules, updates


with open("ex05.txt") as file:
    ex = parse(file)

with open("input05.txt") as file:
    inp = parse(file)

tic()
# -------- Part 1 -----------
print('   PART 1')

rules, updates = inp
result = 0
incorrect_updates = []  # for part 2

for update in updates:
    correct = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not update.index(rule[0]) < update.index(rule[1]):
                correct = False
                incorrect_updates.append(update)  # for part 2
                break
    if correct:
        result += update[len(update) // 2]

print(result)
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

result = 0

for update in updates:
    if update not in incorrect_updates: continue
    correct = False
    rule_n = 0
    while not correct:
        rule = rules[rule_n]
        l = rule[0]
        r = rule[1]
        if l in update and r in update:
            id_l = update.index(l)
            id_r = update.index(r)
            if not id_l < id_r:
                update[id_l], update[id_r] = update[id_r], update[id_l]
                rule_n = 0
                continue
        rule_n += 1
        if rule_n == len(rules):
            result += update[len(update) // 2]
            correct = True
print(result)
toc('Part 2 done in')
