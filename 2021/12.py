from tictoc import tic, toc
from collections import defaultdict, Counter

tic()

with open("input12.txt") as file:
    inp = [line.strip().split('-') for line in file]
# print(inp)

dic = defaultdict(list)
for e in inp:
    dic[e[0]].append(e[1])
    dic[e[1]].append(e[0])
for key in dic:
    dic[key].sort()
# print(dic)


def path_finder(cave, visited):
    visited.append(cave)
    paths = []
    for future_cave in dic[cave]:
        cond = True
        c = Counter(visited)
        for e in c:
            if e.islower() and c[e] >= 2 :
                if future_cave.islower() and c[future_cave] + 1 >= 2:
                    cond = False
        if cond and future_cave != 'start':
            if future_cave == 'end':
                paths.append([cave,future_cave])
            else:
                future_paths = path_finder(future_cave, visited.copy())
                for i in range(len(future_paths)):
                    path = future_paths[i].copy()
                    path.insert(0, cave)
                    future_paths[i] = path
                paths.extend(future_paths)
    return paths

paths = path_finder('start', [])
# for path in paths:
#     print(','.join(path))

print(len(paths))

toc('Terminée en')