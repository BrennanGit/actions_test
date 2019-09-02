import sys
import math


def wrap_string(to_wrap, border='#', full=False,
                top=False, sides=False, bottom=True):
    """Take a string and return it with borders"""
    if len(to_wrap) == 0:
        return ''
    if full:
        bottom, top, sides = True, True, True
    result = ''
    lpad = ' ' * len(border)
    lines = to_wrap.splitlines()
    longest_line = max(lines, key=lambda x: len(x))
    length = len(longest_line)
    print(length)

    if sides:
        length += 2 * len(border) + 2 * len(lpad)
    if top:
        result += border * math.ceil(length / len(border))
    for line in lines:
        print(len(line))
        if sides:
            rpad = ' ' * (length - len(line) - 2 * len(border) - len(lpad) + (length % len(border)))
            result += '\n{0}{1}{2}{3}{0}'.format(border, lpad, line, rpad,)
        else:
            result += '\n{}'.format(line)
    result += '\n'
    if bottom:
        result += border * math.ceil(length / len(border))

    return result


if __name__ == '__main__':
    print()
    print(wrap_string(' '.join(sys.argv[1:]), full=True, border='[]'))
    print()
    print(wrap_string('a\nstring\nwith\nlines', full=True, border='[]'))
