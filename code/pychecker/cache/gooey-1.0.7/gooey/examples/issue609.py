from gooey import Gooey, GooeyParser
from argparse import ArgumentParser

@Gooey()
def main():
    base_parser = GooeyParser(add_help=False)
    base_parser.add_argument("a_file", widget="FileChooser")

    parser = GooeyParser(parents=[base_parser])
    parser.add_argument("a_file", widget="FileChooser")

    print(parser.parse_args())


if __name__ == "__main__":
    main()