from typing import Tuple, List, Set

from tictoc import tic, toc
import re

tic()


def parse_file(path):
    with open(path) as file:
        inp = file.read().strip()
    inp = [scan.strip().split('\n') for scan in re.split(r'--- scanner [0-9]* ---', inp)]
    del inp[0]
    inp = [{tuple(int(n) for n in c.split(',')) for c in s} for s in inp]
    return inp


ex = parse_file('ex19.txt')
inp = parse_file('input19.txt')
# print(inp)
# print(ex)
ex_result = 79

DETECTION_RANGE = 1000

# -------- Part 1 -----------
print('   PART 1')


def rotations(coords):
    rotations_list = []
    rot_matrix = [[1, -1, -1, 1],
                  [1, 1, -1, -1],
                  [1, -1, 1, -1]]
    for i in range(3):
        temp_x = coords[i % 3]
        temp_y = -coords[(i + 1) % 3]
        temp_z = -coords[(i + 2) % 3]
        for k in range(4):
            rotations_list.append((rot_matrix[0][k] * temp_x, rot_matrix[1][k] * temp_y, rot_matrix[2][k] * temp_z))
            rotations_list.append((rot_matrix[1][k] * temp_y, rot_matrix[0][k] * temp_x, - rot_matrix[2][k] * temp_z))
    return rotations_list


r = rotations((1, 2, 3))


def rotate_set(iterable, nrot):
    new = set()
    for e in iterable:
        new.add(rotations(e)[nrot])
    return new


def translate_set(iterable, x, y, z):
    new = set()
    for e in iterable:
        new.add((e[0] + x, e[1] + y, e[2] + z))
    return new


def find_inter_one_coord(rot, i, translation, current_coords1, rotated_coords2):
    c1 = {e[i] for e in current_coords1}
    c2 = {e[rot][i] + translation for e in rotated_coords2}
    inters = c1.intersection(c2)
    if len(inters) > 0:
        current_coords1_copy = current_coords1.copy()
        for c in current_coords1:
            if c[i] not in inters:
                current_coords1_copy.remove(c)
        return current_coords1_copy
    return set()


def find_overlapping(coords1, coords2):
    rotated_coords2 = []
    for c2 in coords2:
        rotated_coords2.append(rotations(c2))

    for rot in range(24):
        # cprint(f'rot {rot}', color='bright')
        for x in range(- 2 * DETECTION_RANGE, 2 * DETECTION_RANGE + 1):
            current_coords_x = set(coords1)
            current_coords_x = find_inter_one_coord(rot, 0, x, current_coords_x, rotated_coords2)
            if len(current_coords_x) >= 12:
                # print(f'x = {x}')
                for y in range(- 2 * DETECTION_RANGE, 2 * DETECTION_RANGE + 1):
                    current_coords_y = current_coords_x.copy()
                    current_coords_y = find_inter_one_coord(rot, 1, y, current_coords_y, rotated_coords2)
                    if len(current_coords_y) >= 12:
                        # print(f'y = {y}')
                        for z in range(- 2 * DETECTION_RANGE, 2 * DETECTION_RANGE + 1):
                            current_coords_z = current_coords_y.copy()
                            current_coords_z = find_inter_one_coord(rot, 2, z, current_coords_z, rotated_coords2)
                            if len(current_coords_z) >= 12:
                                # print(f'z = {z}')
                                return rot, x, y, z, current_coords_z


def recursive_overlapping(scanner_id: int, scanners_list: List[Set[Tuple[int]]],
                          visited_scanner_ids: Set = None):
    if visited_scanner_ids is None:
        visited_scanner_ids = set()
    visited_scanner_ids.add(scanner_id)
    transformation_associations = {}
    scanner = scanners_list[scanner_id]
    for o in range(len(scanners_list)):
        if o not in visited_scanner_ids and scanner_id != o:
            other_scanner = scanners_list[o]
            overlap = find_overlapping(scanner, other_scanner)
            if overlap is not None:
                print(f"found overlapping between {scanner_id} and {o}: {overlap[:-1]}")
                rot, x, y, z, b = overlap
                transformation_associations[o] = [(rot, x, y, z)]
                nested_associations = recursive_overlapping(o, scanners_list, visited_scanner_ids)
                if len(nested_associations) != 0:
                    for i in nested_associations:
                        nested_associations[i].append((rot, x, y, z))
                        transformation_associations[i] = nested_associations[i]
    return transformation_associations


assert rotations((1, 2, 3))[5] == list(rotate_set({(1, 2, 3)}, 5))[0]
assert translate_set({(1, 2, 3)}, 3, 2, 1) == {(4, 4, 4)}
assert translate_set(rotate_set({(1, 2, 3)}, 5), 2, 4, 3) == {(4, 3, 6)}


def get_all_beacons(transformations, scanners_list):
    beacons = set()
    scanners = []
    for scanner_id in transformations:
        current_beacon = scanners_list[scanner_id].copy()
        scan_coords = (0, 0, 0)
        for rot, x, y, z in transformations[scanner_id]:
            scan_coords = rotations(scan_coords)[rot]
            current_beacon = rotate_set(current_beacon, rot)
            scan_coords = (scan_coords[0] + x, scan_coords[1] + y, scan_coords[2] + z)
            current_beacon = translate_set(current_beacon, x, y, z)

        scanners.append(scan_coords)
        beacons = beacons.union(current_beacon)
    beacons = beacons.union(scanners_list[0])
    return beacons, scanners


def solve_part_1(inp):
    asso = recursive_overlapping(0, inp)
    all_beacons, scanners = get_all_beacons(asso, inp)
    return len(all_beacons)


print(solve_part_1(inp))

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def find_max_dist(beacons_set):
    all_beacons_list = list(beacons_set)
    max_dist = 0
    for i in range(len(all_beacons_list)):
        for j in range(i + 1, len(all_beacons_list)):
            distance = dist(all_beacons_list[i], all_beacons_list[j])
            if distance > max_dist:
                max_dist = distance
                max_coords = [all_beacons_list[i], all_beacons_list[j]]
    # print(max_coords)
    return max_dist


def solve_part_2(inp):
    asso = recursive_overlapping(0, inp)
    all_beacons, scanners = get_all_beacons(asso, inp)
    # print(scanners)
    return find_max_dist(scanners)


print(solve_part_2(inp))
toc('Partie 2 terminée en')
