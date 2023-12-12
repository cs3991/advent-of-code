import collections
import sys
import threading
from itertools import islice

from tictoc import tic, toc

with open("ex10.txt") as file:
    ex: tuple[tuple[str]] = tuple(tuple(line.strip()) for line in file if line.strip() != '')

with open("input10.txt") as file:
    inp: tuple[tuple[str]] = tuple(tuple(line.strip()) for line in file if line.strip() != '')
# inp = ex
# -------- Part 1 -----------
print('   PART 1')
tic()

connections = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, 1), (-1, 0)),
    'F': ((0, 1), (1, 0)),
    'S': ((0, -1), (0, 1), (-1, 0), (1, 0))
}


class Tile:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.symbol = inp[self.y][self.x]

    _direction_to_coordinates = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    def get_connection_coordinates(self, only_directions=('N', 'S', 'E', 'W')) -> tuple[tuple[int]]:

        if self.symbol != '.':
            connections_coord = list(connections[self.symbol])
            result = []
            for dx, dy in connections_coord:
                if (0 <= dx + self.x < len(inp[self.y])
                        and 0 <= dy + self.y < len(inp)):
                    result.append((dx, dy))
            return tuple(result)
        else:
            return tuple()

    def get_connected_tiles(self, ) -> tuple['Tile', ...]:
        if self.symbol != 'S':
            return tuple(Tile(self.x + c[0], self.y + c[1]) for c in
                         self.get_connection_coordinates())
        else:
            connected_tiles = []
            for dx, dy in self.get_connection_coordinates():
                new_tile = Tile(self.x + dx, self.y + dy)
                if Tile(self.x, self.y) in new_tile.get_connected_tiles():
                    connected_tiles.append(new_tile)
        return tuple(connected_tiles)

    def get_adjacent_tiles(self, only_directions=('N', 'S', 'E', 'W')):
        result = []
        for direction in only_directions:
            dx, dy = Tile._direction_to_coordinates[direction]
            if (0 <= dx + self.x < len(inp[self.y])
                    and 0 <= dy + self.y < len(inp)):
                result.append(Tile(dx + self.x, dy + self.y))
        return result

    def __repr__(self) -> str:
        return f"Tile({self.x}, {self.y}) : '{self.symbol}'"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


# Search for start position:
sx = None
sy = None
for y in range(len(inp)):
    try:
        sx = inp[y].index('S')
        sy = y
        break
    except:
        continue

# Find the main loop:
start_tile = Tile(sx, sy)
current_tile = start_tile
visited_tiles = {current_tile}
current_tile = current_tile.get_connected_tiles()[0]
number_of_steps = 1
loop_finished = False
while not loop_finished:
    visited_tiles.add(current_tile)
    connected_tiles = current_tile.get_connected_tiles()
    if connected_tiles[0] not in visited_tiles:
        current_tile = connected_tiles[0]
        assert connected_tiles[1] in visited_tiles
    else:
        if connected_tiles[1] in visited_tiles:
            loop_finished = True
        current_tile = connected_tiles[1]
    number_of_steps += 1
print(number_of_steps // 2)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
# Search for start position:
sx = None
sy = None
for y in range(len(inp)):
    try:
        sx = inp[y].index('S')
        sy = y
        break
    except:
        continue

# Find the main loop:
start_tile = Tile(sx, sy)
ext_surf = set()
int_surf = set()
for current_tile in reversed(start_tile.get_connected_tiles()):
    loop_list = [start_tile]
    loop_set = {start_tile}  # set corresponding to the list above, used for 'in' operation for speed
    number_of_steps = 1
    # output = [list(line) for line in inp]
    loop_finished = False
    while not loop_finished:
        # cprint(number_of_steps, color='yellow')
        # print(current_tiles)
        # output[tile.y][tile.x] = str(number_of_steps)
        loop_set.add(current_tile)
        loop_list.append(current_tile)
        connected_tiles = current_tile.get_connected_tiles()
        if connected_tiles[0] not in loop_set:
            current_tile = connected_tiles[0]
            assert connected_tiles[1] in loop_set
        else:
            if connected_tiles[1] in loop_set:
                loop_finished = True
            current_tile = connected_tiles[1]
            # assert connected_tiles[1] not in visited_tiles
        number_of_steps += 1


    # find an empty tile on the border of the map:
    # it is assured not to be part of the enclosed surface.
    # Then spread to the adjacent tiles until reaching the loop frontier
    # The tile on the loop should be included

    def sliding_window(iterable, n):
        # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
        it = iter(iterable)
        window = collections.deque(islice(it, n - 1), maxlen=n)
        for x in it:
            window.append(x)
            yield tuple(window)


    sys.setrecursionlimit(10000)

    visited = set()
    ext = False


    def visit_surface_tiles(from_tile: Tile):
        global ext
        if from_tile not in loop_set and from_tile.x == 0:
            # or from_tile.x == len(inp[0]) or from_tile.y == 0 or from_tile.y == len(inp)
            ext = True
        if from_tile in loop_set or from_tile in visited:
            return []
        visited.add(from_tile)
        result = []
        for tile in from_tile.get_adjacent_tiles():
            result.extend(visit_surface_tiles(tile))
        return result


    for previous_tile, next_tile in sliding_window(loop_list, 2):
        dx, dy = (next_tile.y - previous_tile.y, - next_tile.x + previous_tile.x)
        for tile in (previous_tile, next_tile):
            if 0 <= tile.x + dx < len(inp[0]) and \
                    0 <= tile.y + dy < len(inp):
                interior_tile = Tile(tile.x + dx, tile.y + dy)
                sys.setrecursionlimit(100000)
                threading.stack_size(200000000)
                thread = threading.Thread(target=lambda: visit_surface_tiles(interior_tile))
                thread.start()

    if ext:
        ext_surf = visited.difference(loop_set)
    else:
        int_surf = visited.difference(loop_set)

print(len(int_surf))
# 260 < solution < 937
toc('Part 2 done in')
