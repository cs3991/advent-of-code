def hilite(string, color, bold=False):
    attr = []
    match color:
        case 'green':
            attr.append('32')
        case 'red':
            attr.append('31')
        case 'blue':
            attr.append('34')
        case 'yellow':
            attr.append('33')
        case 'bright':
            attr.append('90')
        case 'magenta':
            attr.append('35')
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)


def cprint(value: object, color: str, end: str = None, bold: bool = False):
    """
    Print a single string to terminal. Accepted colors: green, red, blue, yellow, bright, magenta.
    :param bold:
    :param end:
    :param value:
    :param color:
    :return:
    """
    print(hilite(value, color, bold), end=end)
