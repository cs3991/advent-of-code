import re

from tictoc import tic, toc

with open("ex06.txt") as file:
    ex = [line for line in file]

with open("input06.txt") as file:
    inp = [line for line in file]
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')

# print(input)
# input = ex
races = []
for n, l in enumerate(inp):
    l = l.strip()
    matches = re.findall(pattern=r"([0-9]+)", string=l)
    for m, i in enumerate(matches):
        if n == 0:
            races.append([None, None])
        races[m][n] = int(i)
solution = 1
for race in races:
    number__of_ways_to_beat = 0
    duration = race[0]
    record_distance = race[1]
    for time_pressed in range(duration):
        distance = (duration - time_pressed) * time_pressed
        if distance > record_distance:
            number__of_ways_to_beat += 1
    solution *= number__of_ways_to_beat
print(solution)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
race = []
for l in inp:
    s = l.split(":")[1].replace(" ", "")
    race.append(int(s))

number__of_ways_to_beat = 0
duration = race[0]
record_distance = race[1]
for time_pressed in range(duration):
    distance = (duration - time_pressed) * time_pressed
    if distance > record_distance:
        number__of_ways_to_beat += 1
print(number__of_ways_to_beat)

toc('Part 2 done in')
