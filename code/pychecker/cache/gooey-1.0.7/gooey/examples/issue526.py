import sys
from gooey import Gooey, GooeyParser


@Gooey()
def gui():
    parser = GooeyParser(description='Process')

    parser.add_argument(
        '-f', '--foo',
        metavar='Some Flag1',
        action='store_true',
        default=True)  # BUG: always yields True!  (works only when default=False)

    parser.add_argument(
        '-b', '--bar',
        metavar='Some Flag2',
        action='store_false',
        default=False)  # BUG: always yields False!  (works only when default=True)

    print(sys.argv)
    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    var = gui()
    print('var:', var)  # <--watch output to see the bug
