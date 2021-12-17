from tictoc import tic, toc
import numpy as np
from PIL import Image, ImageColor

tic()

with open("input15.txt") as file:
    inp = [[int(n) for n in line.strip()] for line in file]
# print(inp)

def solve(matrice):
    N = len(matrice)
    visited = set()
    paths = [(0, (0, 0))]  # elements : [risk, coords of last position]
    i = 0
    neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while True:
        paths_copy = paths.copy()
        for path in paths_copy:
            coord = path[1]
            risk = path[0]
            if risk == i:
                for k in range(4):
                    fut_coord = (coord[0] + neighbors[k][0], coord[1] + neighbors[k][1])
                    if fut_coord not in visited:
                        if max(fut_coord) < N and min(fut_coord) >= 0:
                            new_risk = risk + matrice[fut_coord[0]][fut_coord[1]]
                            paths.append([new_risk, fut_coord])
                            visited.add(fut_coord)
                paths.remove(path)
            if coord == (N - 1, N - 1):
                return risk
        i += 1

# -------- Part 1 -----------
print('   PART 1')
print(solve(inp))

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

mat = np.array(inp)
for i in range(0, 5):
    line = mat.copy()
    for j in range(1, 5):
        line = np.concatenate((line, (mat + j - 1) % 9 + 1), axis=1)
    if i == 0:
        big = line.copy()
    else:
        big = np.concatenate((big, (line + i - 1) % 9 + 1), axis=0)

print(solve(big))

toc('Partie 2 terminée en')















# while not_found:
#     paths_copy = paths.copy()
#     # print(i)
#     for path in paths_copy:
#         print(path)
#         # if path[0] == i:
#         for dir in range(2):
#             fut_coord = (path[1][0] + dir, path[1][1] + 1 - dir)
#             if fut_coord not in visited and max(fut_coord) < N and min(fut_coord) >= 0:
#                 # if not in border
#                 # if fut_coord[0] + fut_coord[1] > i / 4 - 100:
#                 new_risk = path[0] + big[fut_coord[0]][fut_coord[1]]
#                 paths.append((new_risk, fut_coord))
#                 visited.add(fut_coord)
#         paths.remove(path)
#         if path[1] == (N - 1, N - 1):
#             print(path[0])
#             not_found = False
#     # paths.sort(key=lambda e: (e[1][0] + e[1][1]) / e[0], reverse=True)
#     # print(len(paths))
#     # print(paths[0])
#     # print(paths)
#     # paths = paths[-400:]
#     if i % 5 == 0:
#         im = Image.new('1', (N, N))
#         for t in visited:
#             im.putpixel(t, ImageColor.getcolor('white', '1'))
#         ims.append(im.convert('P'))
#     # im.save('img/' + str(i) + '.png')
#     i += 1


# fp_in = "img/*.png"
# fp_out = "img/animation2.gif"
# # img, *imgs = [Image.open(f).convert('P') for f in sorted(glob.glob(fp_in), key=lambda s : int(s[4:-4]))[::5]]
# img, *imgs = ims
# img.save(fp=fp_out, format='GIF', append_images=imgs,
#          save_all=True, duration=20, loop=0)








# def neighbors(n):
#     im = Image.new('1', (N, N))
#     for t in visited:
#         im.putpixel(t, ImageColor.getcolor('white', '1'))
#     ims.append(im.convert('P'))
#
#     for dir in range(2):
#         print('n', n)
#         fut_coord = (n[0][0] + dir, n[0][1] + 1 - dir)
#         if max(fut_coord) < N and min(fut_coord) >= 0:
#             visited.add(fut_coord)
#             yield (fut_coord, big[fut_coord])
#
# def cost(a, b):
#     ca = a[0]
#     cb = b[0]
#     return abs(ca[0] - cb[0] + ca[1] - cb[1])
#
# def distance(a, b):
#     return b[1]
#
# solution = astar.find_path(((0, 0), big[0, 0]),
#                            ((N - 1, N - 1), big[(N - 1, N - 1)]),
#                            neighbors_fnct=neighbors,
#                            distance_between_fnct=distance,
#                            heuristic_cost_estimate_fnct=cost)
# count = 0
# imsol = Image.new('1', (N, N))
# # for t in visited:
# #     imsol.putpixel(t, ImageColor.getcolor('white', '1'))
# for n in list(solution):
#     count += n[1]
#     imsol.putpixel((n[0][1], n[0][0]), ImageColor.getcolor('red', 'L'))
# imsol.save('img/solution.png')
#
# print(count)
#
#
