from tictoc import tic, toc
from collections import defaultdict, Counter
from cprint import cprint

tic()


def parse(filename):
    with open(filename) as file:
        inp = file.readline().strip()
    # print(inp)
    return f'{int(inp, 16):0>{len(inp) * 4}b}'


inp = parse('input16.txt')

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
        match encod:
            case 'V':  # Version
                version += int(raw[i]) * 2 ** (2 - n_bit)
                if n_bit < 2:
                    n_bit += 1
                else:  # si fin de version
                    n_bit = 0
                    version_sum += version
                    encod = 'T'
            case 'T':  # Type
                type += int(raw[i]) * 2 ** (2 - n_bit)
                if n_bit < 2:
                    n_bit += 1
                else:  # si fin de type
                    n_bit = 0
                    if type == 4:
                        encod = 'A'
                    else:
                        encod = 'I'
            case 'A':  # Literal
                if n_bit == 0:  # premier bit indique s'il y a d'autres nombres après
                    literal.append(0)
                    if raw[i] == '0':
                        literal_end = True
                if n_bit > 0:
                    literal[-1] += int(raw[i]) * 2 ** (4 - n_bit)
                if n_bit == 4:
                    if literal_end:
                        for k in range(len(literal)):
                            value += literal[k] << (len(literal) - 1 - k) * 4
                        return version_sum, i, value
                    n_bit = -1
                n_bit += 1
            case 'I':
                if raw[i] == '0':
                    encod = 'L'
                else:
                    encod = 'N'
            case 'L':
                len_sub_pack += int(raw[i]) * 2 ** (14 - n_bit)
                if n_bit < 14:
                    n_bit += 1
                else:
                    end_sub_pack = i + len_sub_pack
                    while i < end_sub_pack:
                        v, i, value_add = decod_packet(raw, i)
                        version_sum += v
                        values.append(value_add)
                    value = operate(values, type)
                    return version_sum, i, value
            case 'N':
                n_sub_pack += int(raw[i]) * 2 ** (10 - n_bit)
                if n_bit < 10:
                    n_bit += 1
                else:
                    for k in range(n_sub_pack):
                        v, i, value_add = decod_packet(raw, i)
                        version_sum += v
                        values.append(value_add)
                    value = operate(values, type)
                    return version_sum, i, value


def part_1(raw):
    return decod_packet(raw)[0]


print(part_1(inp))

toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')


def part_2(raw):
    return decod_packet(raw)[2]


print(part_2(inp))

toc('Partie 2 terminée en')
