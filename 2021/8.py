from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input8.txt") as input_file:
    input_list = [line.split(' | ') for line in input_file]
# print(input_list)

# -------- Part 1 -----------
DIC = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

SEG = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'},
}
inter6 = SEG[0].intersection(SEG[6]).intersection(SEG[9])
inter5 = SEG[2].intersection(SEG[3]).intersection(SEG[5])

print('   PART 1')
ez = [2, 4, 3, 7]
count = 0
for line in input_list:
    out_val = line[1]
    for segs in out_val.split():
        if len(segs) in ez:
            count += 1
print(count)

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

total = 0
for line in input_list:
    lut = defaultdict(lambda: {'a', 'b', 'c', 'd', 'e', 'f', 'g'})
    for segs in line[0].split() + line[1].split():

        poss_seg = set()
        for i in DIC:
            if len(segs) == DIC[i]:  # nombre de segments correspondent
                # print(i)
                poss_seg = poss_seg.union(SEG[i])
        # Si on est dans le cas simple (1 seule association)
        if len(poss_seg) == len(segs):
            for seg in SEG[8].difference(set(segs)):
                lut[seg].difference_update(poss_seg)
        for seg in segs:
            lut[seg].intersection_update(poss_seg)
        # Si la longueur est de 6, on peut supprimer les segments communs à 0, 6 et 9 des autres sets
        if len(segs) == 6:
            for seg in SEG[8].difference(segs):
                lut[seg].difference_update(inter6)
        # Si la longueur est de 5, on peut supprimer les segments communs à 2, 3 et 5 des autres sets
        if len(segs) == 5:
            for seg in SEG[8].difference(segs):
                lut[seg].difference_update(inter5)
        # Si on trouve une association, on peut supprimer le segment dans les autres sets
        for seg in lut:
            if len(lut[seg]) == 1:
                for lut_set in lut.values():
                    if len(lut_set) != 1:
                        lut_set.difference_update(lut[seg])

    number = ''
    for segs in line[1].split():  # Association à un chiffre
        for i in DIC:
            num_set = set()
            for seg in segs:
                num_set = num_set.union(lut[seg])
            if SEG[i].issubset(num_set) and len(SEG[i]) == len(segs):
                number += str(i)
    total += int(number)
print(total)

toc('Partie 2 terminée en')
