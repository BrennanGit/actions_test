import sys


def wrap_string(to_wrap, border='#', full=False,
                top=False, sides=False, bottom=True):
    """Take a string and return it with borders"""
    if len(to_wrap) == 0:
        return ''
    if full:
        bottom, top, sides = True, True, True
    result = ''
    lines = to_wrap.splitlines()
    longest_line = max(lines, key=lambda x: len(x))
    length = len(longest_line) // len(border)

    if sides:
        length += 2 // len(border) + 2
    if top:
        result += border * length
    for line in lines:
        if sides:
            padding = length - len(line) - 2 * len(border) - 1  # other space
            result += '\n{0} {1}{2}{0}'.format(border, line, ' '*padding)
        else:
            result += '\n{}'.format(line)
    result += '\n'
    if bottom:
        result += border * length

    return result


if __name__ == '__main__':
    print()
    print(wrap_string(' '.join(sys.argv[1:]), full=True))
    print(wrap_string('multiline\nstring', full=True))
