from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input14.txt") as file:
    polymer = file.readline().strip()
    file.readline()
    inp = [line.strip().split(' -> ') for line in file]
assoc = {}
for e in inp:
    assoc[e[0]] = e[1]

polymer = polymer.center(len(polymer) + 2, '#')
pol_pairs = []
for i in range(len(polymer) - 1):
    pol_pairs.append(polymer[i] + polymer[i + 1])

pairs_count = Counter(pol_pairs)

for step in range(40): # ou 10 pour partie 1
    pairs_count_copy = pairs_count.copy()
    for pair in pairs_count_copy:
        if pair in assoc:
            pairs_count[pair[0] + assoc[pair]] += pairs_count_copy[pair]
            pairs_count[assoc[pair] + pair[1]] += pairs_count_copy[pair]
            pairs_count[pair] -= pairs_count_copy[pair]
letter_count = defaultdict(int)
for pair in pairs_count:
    letter_count[pair[0]] += pairs_count[pair] / 2
    letter_count[pair[1]] += pairs_count[pair] / 2
del letter_count['#']

print(max(letter_count.values()) - min(letter_count.values()))

toc('Terminée en')
