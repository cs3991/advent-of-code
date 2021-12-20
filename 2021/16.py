from tictoc import tic, toc
from collections import defaultdict, Counter
from cprint import cprint

tic()


def parse(filename, multi=False):
    with open(filename) as file:
        inp = [line.strip() for line in file]
    # print(inp)
    raw = []
    for i in range(len(inp)):
        raw.append(f'{int(inp[i], 16):0>{len(inp[i]) * 4}b}')
    if not multi:
        raw = raw[0]
    return raw



inp = parse('input16.txt')
ex = parse('ex16.txt', multi=True)
ex1 = 31
ex2 = 1

# -------- Part 1 -----------
print('   PART 1')

def operate(values, type):
    match type:
        case 0:
            return sum(values)
        case 1:
            r = 1
            for k in values:
                r *= k
            return r
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            assert len(values) == 2
            return 1 if values[0] > values[1] else 0
        case 6:
            assert len(values) == 2
            return 1 if values[0] < values[1] else 0
        case 7:
            assert len(values) == 2
            return 1 if values[0] == values[1] else 0
        case _:
            assert False


def decod_packet(raw, start=-1, verbose=False):
    value = 0
    version_sum = 0
    i = start
    encod = 'V'
    n_bit = 0
    version = 0
    type = 0
    literal = []
    literal_end = False
    len_sub_pack = 0
    n_sub_pack = 0
    values = []

    while True:
        i += 1
        cprint('\n' + f'{str(i):0>4}', 'bright', end='|') if verbose else ''
        cprint(raw[i], 'blue', end='|') if verbose else ''
        print(encod, end='|') if verbose else ''
        cprint(f'{n_bit:0>2}', 'yellow', end='|  ') if verbose else ''
        match encod:
            case 'V':  # Version
                version += int(raw[i]) * 2 ** (2 - n_bit)
                if n_bit < 2:
                    n_bit += 1
                else:  # si fin de version
                    n_bit = 0
                    cprint(f'version : {version}', 'green', end='') if verbose else ''
                    version_sum += version
                    encod = 'T'
            case 'T':  # Type
                type += int(raw[i]) * 2 ** (2 - n_bit)
                if n_bit < 2:
                    n_bit += 1
                else:  # si fin de type
                    cprint(f'type : {type} : ', 'green', end='') if verbose else ''
                    n_bit = 0
                    if type == 4:
                        encod = 'A'
                        cprint(f'Literal', 'green', end='') if verbose else ''
                    else:
                        cprint(f'Operator', 'green', end='') if verbose else ''
                        encod = 'I'
            case 'A':  # Literal
                if n_bit == 0:  # premier bit indique s'il y a d'autres nombres après
                    literal.append(0)
                    cprint(f"{'end' if raw[i] == '0' else 'continue'}", 'magenta', end='') if verbose else ''
                    if raw[i] == '0':
                        literal_end = True
                if n_bit > 0:
                    literal[-1] += int(raw[i]) * 2 ** (4 - n_bit)
                if n_bit == 4:
                    cprint(f'literal : {literal[-1]}', 'green', end='') if verbose else ''
                    if literal_end:
                        for k in range(len(literal)):
                            value += literal[k] << (len(literal) - 1 - k) * 4
                        print(value) if verbose else ''
                        return version_sum, i, value
                    n_bit = -1
                n_bit += 1
            case 'I':
                if raw[i] == '0':
                    encod = 'L'
                    cprint('codé par longueur', 'green', end='') if verbose else ''
                else:
                    encod = 'N'
                    cprint('codé par nombre', 'green', end='') if verbose else ''
            case 'L':
                len_sub_pack += int(raw[i]) * 2 ** (14 - n_bit)
                if n_bit < 14:
                    n_bit += 1
                else:
                    cprint(f'longueur des sous-packets : {len_sub_pack}', 'green', end='') if verbose else ''
                    end_sub_pack = i + len_sub_pack
                    while i < end_sub_pack:
                        v, i, value_add = decod_packet(raw, i)
                        version_sum += v
                        values.append(value_add)
                    value = operate(values, type)
                    return  version_sum, i, value
            case 'N':
                n_sub_pack += int(raw[i]) * 2 ** (10 - n_bit)
                if n_bit < 10:
                    n_bit += 1
                else:
                    cprint(f'nombre de sous packets : {n_sub_pack}', 'green', end='') if verbose else ''
                    for k in range(n_sub_pack):
                        v, i, value_add = decod_packet(raw, i)
                        version_sum += v
                        values.append(value_add)
                    value = operate(values, type)
                    return  version_sum, i, value


def part_1(raw):
    return decod_packet(raw)[0]


solution_1_ex = part_1(ex[0])
print()
if solution_1_ex == ex1:
    cprint('Test sur l\'exemple OK', 'green', bold=True)
else:
    cprint(f'Test échoué : valeur trouvé : {solution_1_ex}, valeur attendue : {ex1}', 'red', bold=True)


# print('\n', part_1(inp))




toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')

def part_2(raw):
    return decod_packet(raw)[2]

ex_sol = [3,
54,
7,
9,
1,
0,
0,
1]

for k in range(len(ex)):
    cprint(part_2(ex[k]), 'green', end=' ')
    cprint(ex_sol[k], 'magenta')

print(part_2(inp))

# if solution_2_ex == ex2:
#     cprint('Test sur l\'exemple OK', 'green', bold=True)
# else:
#     cprint(f'Test échoué : valeur trouvé : {solution_2_ex}, valeur attendue : {ex2}', 'red', bold=True)


toc('Partie 2 terminée en')
