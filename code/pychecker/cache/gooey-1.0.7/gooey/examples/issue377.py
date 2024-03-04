import sys
import argparse
from gooey import Gooey


@Gooey
def main():
    """Demonstrate [metavar='<FILE>', type=argparse.FileType()] issue."""
    parser = argparse.ArgumentParser(
        description="Show [metavar='<FILE>', type=argparse.FileType()] issue.",
        add_help=False,
        usage="test.py -u username -p password [options]")
    parser.add_argument('-o',
                        metavar='<FILE>',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='output data file [stdout]')

    args = parser.parse_args()
    print(args.o)
    for i in range(10):
        args.o.write(str(i))


if __name__ == '__main__':
    main()