from collections import defaultdict

from tictoc import tic, toc

with open("ex15.txt") as file:
    ex = file.read().strip().split(',')

with open("input15.txt") as file:
    inp = file.read().strip().split(',')

tic()
# -------- Part 1 -----------
print('   PART 1')
solution = 0
for step in inp:
    current_value = 0
    for c in step:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    solution += current_value
print(solution)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')
boxes: dict[int, list[tuple[str, int]]] = defaultdict(list)
for step in inp:
    hash = 0
    lens_label = step.split('=')[0] if '=' in step else step.split('-')[0]
    for c in lens_label:
        hash += ord(c)
        hash *= 17
        hash %= 256
    if '-' in step:
        lens_label = step.split('-')[0]
        for box_content in boxes.values():
            for lens_in_box in box_content:
                if lens_in_box[0] == lens_label:
                    box_content.remove(lens_in_box)
    elif '=' in step:
        focal_length = int(step.split('=')[1])
        replaced = False
        box_content = boxes[hash]
        for lens_in_box in box_content:
            if lens_in_box[0] == lens_label:
                index = box_content.index(lens_in_box)
                box_content.remove(lens_in_box)
                box_content.insert(index, (lens_label, focal_length))
                replaced = True
                break
        if not replaced:
            box_content.append((lens_label, focal_length))
    else:
        raise Exception(':(')

solution = 0
for box_index in boxes:
    for i, lens in enumerate(boxes[box_index]):
        solution += (box_index + 1) * (i + 1) * lens[1]
print(solution)

toc('Part 2 done in')
