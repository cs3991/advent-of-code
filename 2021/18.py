from tictoc import tic, toc
import re
from cprint import cprint
from collections import defaultdict, Counter

tic()

with open("input18.txt") as file:
    inp = [line.strip() for line in file]

inp_list = []

# -------- Part 1 -----------
print('   PART 1')


class SnailfishNumber:
    left = None
    right = None

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    @staticmethod
    def parse_text(inp_str):

        def find_corresponding(text: str) -> int:
            count = 0
            for j in range(len(text)):
                if text[j] == '[':
                    count += 1
                elif text[j] == ']':
                    count -= 1
                if count == 0:
                    return j

        def find_int(text: str) -> (int, int):
            k = 0
            n_str = ''
            while re.match('[0-9]', text[k]):
                n_str += text[k]
                k += 1
            return int(n_str), k

        current = SnailfishNumber()
        inp_str = inp_str.removeprefix('[')
        k = 0
        while k < (len(inp_str)):
            if re.match('[0-9]', inp_str[k]):
                n, index = find_int(inp_str[k:])
                current.append(n)
                k += index - 1
            elif inp_str[k] == '[':
                current.append(SnailfishNumber.parse_text(inp_str[k:]))
                k = find_corresponding(inp_str[k:])
            if current.len() == 2:
                return current
            k += 1

    def len(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None or self.right is None:
            return 1
        else:
            return 2

    def append(self, o):
        if self.left is None:
            self.left = o
            return True
        if self.right is None:
            self.right = o
            return True
        else:
            return False

    def to_infix(self, tree=()):
        for k in range(self.len()):
            current = tree + tuple([k])
            element = self[k]
            if type(element) is int:
                yield element, current
            else:
                yield from element.to_infix(current)

    def get_by_path(self, path):
        current = self
        for i in path:
            current = current[i]
        return current

    def set_by_path(self, path, new_value):
        if new_value is None:
            return
        current = self
        for i in path[:-1]:
            current = current[i]
        current[path[-1]] = new_value

    def split(self):
        for num, tree in self.to_infix():
            if num >= 10:
                self.set_by_path(tree, SnailfishNumber(num // 2, num // 2 if num % 2 == 0 else num // 2 + 1))
                # print('after split:', self, sep='    ')
                return True
        return False

    def explode(self):
        list_infix = list(self.to_infix())
        left_path = None
        left_num = None
        for k in range(len(list_infix)):
            num, current_path = list_infix[k]
            if len(current_path) == 5:
                if left_path is not None:
                    left_num = self.get_by_path(left_path)
                if k + 2 >= len(list_infix):
                    right_num = None
                else:
                    right_path = list_infix[k + 2][1]
                    right_num = self.get_by_path(right_path)
                pair = self.get_by_path(current_path[:-1])
                # if pair[0] is num:
                #
                # else:

                if right_num is not None:
                    right_num += pair.right
                    self.set_by_path(right_path, right_num)
                if left_num is not None:
                    left_num += pair.left
                    self.set_by_path(left_path, left_num)

                self.set_by_path(current_path[:-1], 0)
                # print('after explode:', self, sep='  ')
                return True
            left_path = current_path
        return False

    def reduce(self):
        any_operation = True
        while any_operation:
            exploded = self.explode()
            split = False
            if not exploded:
                split = self.split()
            any_operation = exploded or split

    def magnitude(self):
        mag = 0
        if type(self.left) is SnailfishNumber:
            mag += 3 * self.left.magnitude()
        else:
            mag += 3 * self.left
        if type(self.right) is SnailfishNumber:
            mag += 2 * self.right.magnitude()
        else:
            mag += 2 * self.right
        return mag

    @staticmethod
    def sum(list_numbers):
        result = None
        for num in list_numbers:
            if result is None:
                result = num
            else:
                result += num
        return result

    def __getitem__(self, item):
        match item:
            case 0:
                return self.left
            case 1:
                return self.right
            case _:
                raise IndexError

    def __setitem__(self, key, value):
        match key:
            case 0:
                self.left = value
            case 1:
                self.right = value
            case _:
                raise IndexError

    def __add__(self, o):
        result = SnailfishNumber(self.copy(), o.copy())
        result.reduce()
        return result

    def __str__(self):
        return f'[{self.left},{self.right}]'

    def __eq__(self, other):
        return type(self.left) is type(other.left) and \
               type(self.right) is type(other.right) and \
               self.left == other.left and \
               self.right == other.right

    def copy(self):
        if type(self.left) is not int:
            left = self.left.copy()
        else:
            left = self.left
        if type(self.right) is not int:
            right = self.right.copy()
        else:
            right = self.right
        return SnailfishNumber(left=left, right=right)


for line in inp:
    number = SnailfishNumber.parse_text(line)
    inp_list.append(number)

assert SnailfishNumber.parse_text('[1,2]') + SnailfishNumber.parse_text('[[3,4],5]') == SnailfishNumber.parse_text(
    '[[1,2],[[3,4],5]]')

test = SnailfishNumber.parse_text('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]')
test.explode()
assert test == SnailfishNumber.parse_text('[[[[0,7],4],[15,[0,13]]],[1,1]]')

test = SnailfishNumber.parse_text('[[[[0,7],4],[15,[0,13]]],[1,1]]')
test.split()
assert test == SnailfishNumber.parse_text('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')

test = SnailfishNumber.parse_text('[[[[4,3],4],4],[7,[[8,4],9]]]') + SnailfishNumber.parse_text('[1,1]')
test.reduce()
assert test == SnailfishNumber.parse_text('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

test = SnailfishNumber.parse_text('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]') + SnailfishNumber.parse_text(
    '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
test.reduce()
assert test == SnailfishNumber.parse_text('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')

big_example = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''
example_list = [SnailfishNumber.parse_text(line.strip()) for line in big_example.split('\n')]
test = SnailfishNumber.sum(example_list)
assert test == SnailfishNumber.parse_text('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
assert test.magnitude() == 4140

print(SnailfishNumber.sum(inp_list).magnitude())

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')


def part2(l):
    max_mag = 0
    for i in range(len(l)):
        n1 = l[i]
        for j in range(len(l)):
            n2 = l[j]
            if i != j:
                mag = (n1 + n2).magnitude()
                if mag > max_mag:
                    max_mag = mag
    return max_mag


assert part2(example_list) == 3993

print(part2(inp_list))

toc('Partie 2 terminée en')
