import pandas as pd

from tictoc import tic, toc

with open("ex09.txt") as file:
    ex = [[int(i) for i in line.strip().split()] for line in file if line.strip() != '']

with open("input09.txt") as file:
    inp = [[int(i) for i in line.strip().split()] for line in file if line.strip() != '']
# inp = ex
tic()
# -------- Part 1 -----------
print('   PART 1')


def solve(inp):
    dataframes = [pd.DataFrame(data=inp).transpose()]
    while ((dataframes[0] != 0) & ~dataframes[0].isna()).any(axis=None):
        dataframes.insert(0, dataframes[0].diff())
    for i, df in enumerate(dataframes):
        dataframes[i] = pd.concat((df, df.tail(1)), ignore_index=True)
        if i > 0:
            dataframes[i].iloc[-1, :] = df.iloc[-1, :] + dataframes[i - 1].iloc[-1, :]
    return dataframes[-1].iloc[-1, :].sum()


print(solve(inp))
toc('Part 1 (pandas) done in')
solution = 0
for line in inp:
    differences = [line]
    while differences[-1].count(0) != len(differences[-1]):
        new_difference = []
        for i in range(len(differences[-1]) - 1):
            new_difference.append(differences[-1][i + 1] - differences[-1][i])
        differences.append(new_difference)
    for i in range(len(differences) - 1, 0, -1):
        differences[i - 1].append(differences[i - 1][-1] + differences[i][-1])
    solution += differences[0][-1]

print(solution)
toc('Part1 (list) done in')
# -------- Part 2 -----------
print('   PART 2')
inp_reverse = inp.copy()
for l in inp_reverse:
    l.reverse()
print(solve(inp_reverse))

toc('Part 2 done in')
