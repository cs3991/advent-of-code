from tictoc import tic, toc


def parse(file):
    return [list(line.strip()) for line in file]


with open("ex06.txt") as file:
    ex = parse(file)

with open("input06.txt") as file:
    inp = parse(file)

tic()
# -------- Part 1 -----------
print('   PART 1')
map = ex
walls = set()
guard_position = None
directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]
for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        c = line[x]
        if c == '#':
            walls.add((x, y))
        elif c == '^':
            guard_position = (x, y)
            guard_orientation = directions[0]

visited = set()
while 0 <= guard_position[0] < len(map[0]) and 0 <= guard_position[1] < len(map):
    # print(guard_position, guard_orientation)
    visited.add(guard_position)
    new_pos = (guard_position[0] + guard_orientation[0],
               guard_position[1] + guard_orientation[1])
    if new_pos in walls:
        guard_orientation = directions[(directions.index(guard_orientation) + 1) % 4]
        new_pos = (guard_position[0] + guard_orientation[0],
                   guard_position[1] + guard_orientation[1])
    guard_position = new_pos

print(len(visited))
toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

p1_visited = visited.copy()
walls = set()
guard_position = None
for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        c = line[x]
        if c == '#':
            walls.add((x, y))
        elif c == '^':
            guard_position = (x, y)
            guard_orientation = directions[0]


def is_loop(guard_position, guard_orientation, walls):
    vis = set()
    while True:
        if not (0 <= guard_position[0] < len(map[0]) and 0 <= guard_position[1] < len(map)):
            # print(len(visited))
            return False
        if (guard_position, guard_orientation) in vis:
            # print(len(visited))
            return True
        vis.add((guard_position, guard_orientation))
        new_pos = (guard_position[0] + guard_orientation[0],
                   guard_position[1] + guard_orientation[1])
        if new_pos in walls:
            guard_orientation = directions[(directions.index(guard_orientation) + 1) % 4]
        else:
            guard_position = new_pos


result = 0
for position in p1_visited:
    if is_loop(guard_position, guard_orientation, walls.union({position})):
        result += 1

# visited = set()
# while 0 <= guard_position[0] < len(map[0]) and 0 <= guard_position[1] < len(map):
#     print(guard_position, guard_orientation)
#     visited.add((guard_position, guard_orientation))
#     print(len(visited), result)
#     new_pos = (guard_position[0] + guard_orientation[0],
#                guard_position[1] + guard_orientation[1])
#     if new_pos in walls:
#         guard_orientation = directions[(directions.index(guard_orientation) + 1) % 4]
#         new_pos = guard_position
#     if is_loop(guard_position, guard_orientation, walls.union({new_pos}), visited):
#         result += 1
#     guard_position = new_pos

print(result)

toc('Part 2 done in')
