from gooey import Gooey
import argparse

@Gooey
def _main_():
    parent = argparse.ArgumentParser(description="My program")
    parent.add_argument("-g","--global",help="A global variable")
    subparsers = parent.add_subparsers(help="")
    parser_child_a = subparsers.add_parser("childa", help="childa help", parents=[parent],
                                         add_help=False)
    parser_child_a.add_argument("-a",help="a option")

    parser_child_b = subparsers.add_parser("childb", help="childb help", parents=[parent],
                                           add_help=False)
    parser_child_b.add_argument("-b", help="b option")

    parent.parse_args()

if __name__ == '__main__':
    _main_()