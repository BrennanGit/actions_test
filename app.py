import sys


def wrap_string(to_wrap, border='#', full=False,
                top=False, sides=False, bottom=True):
    """Take a string and return it with borders"""
    if full:
        bottom, top, sides = True, True, True
    result = ''
    length = len(to_wrap) // len(border)
    if sides:
        length += 2 // len(border) + 2
    if top:
        result += border * length
    if sides:
        result += '\n{0} {1} {0}\n'.format(border, to_wrap)
    else:
        result += '\n{}\n'.format(to_wrap)
    if bottom:
        result += border * length

    return result


if __name__ == '__main__':
    print()
    print(wrap_string(' '.join(sys.argv[1:]), full=True))
