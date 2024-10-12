from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter

with open("ex16.txt") as file:
    ex = tuple(tuple(line.strip()) for line in file if line.strip() != '')

with open("input16.txt") as file:
    inp = tuple(tuple(line.strip()) for line in file if line.strip() != '')
# inp = ex

tic()
# -------- Part 1 -----------
print('   PART 1')


def next_tiles(x, y, c, dx, dy):
    assert dx == -1 or dx == 0 or dx == 1
    assert dy == -1 or dy == 0 or dy == 1
    assert (dx == 0 and dy != 0) or (dy == 0 and dx != 0)
    match c:
        case '.':
            return [(x + dx, y + dy, dx, dy)]
        case '\\':
            return [(x + dy, y + dx, dy, dx)]
        case '/':
            return [(x - dy, y - dx, -dy, -dx)]
        case '-':
            if dy != 0:
                return [(x - 1, y, -1, 0), (x + 1, y, 1, 0)]
            else:
                return [(x + dx, y + dy, dx, dy)]
        case '|':
            if dx != 0:
                return [(x, y - 1, 0, -1), (x, y + 1, 0, 1)]
            else:
                return [(x + dx, y + dy, dx, dy)]


def get(table, x, y):
    if 0 <= y < len(table) and 0 <= x < len(table[y]):
        return table[y][x]
    return None


start = (0, 0)
start_direction = (1, 0)
current_tiles = [(*start, *start_direction)]
energized = set()
visited = set()
while len(current_tiles) != 0:
    tile = current_tiles[0]
    x, y, dx, dy = tile
    tile_char = get(inp, x, y)
    if tile_char is not None and tile not in visited:
        current_tiles.extend(next_tiles(x, y, tile_char, dx, dy))
        energized.add((x, y))
        visited.add(tile)
    current_tiles.remove(tile)
print(len(energized))

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
solution = 0
for current_tile in ([(0, i, 1, 0) for i in range(len(inp))] +
                     [(len(inp[0]) - 1, i, -1, 0) for i in range(len(inp))] +
                     [(i, 0, 0, 1) for i in range(len(inp))] +
                     [(i, len(inp[0]) - 1, 0, -1) for i in range(len(inp))]):
    energized = set()
    visited = set()
    current_tiles = [current_tile]
    while len(current_tiles) != 0:
        tile = current_tiles[0]
        x, y, dx, dy = tile
        tile_char = get(inp, x, y)
        if tile_char is not None and tile not in visited:
            current_tiles.extend(next_tiles(x, y, tile_char, dx, dy))
            energized.add((x, y))
            visited.add(tile)
        current_tiles.remove(tile)
    if len(energized) > solution:
        solution = len(energized)
print(solution)

toc('Part 2 done in')
