import wx
import sys
import time

from gooey import Gooey, GooeyParser, constants


@Gooey
def gooey_app():
    parser = GooeyParser()

    group = parser.add_mutually_exclusive_group(required=False, gooey_options={
        'initial_selection': 0
    })
    group.add_argument('-f', '--file', help="Chose a File")
    group.add_argument('-d', '--dir', help="Chose a directory")


    args = parser.parse_args()


if __name__ == '__main__':
    sys.exit(gooey_app())