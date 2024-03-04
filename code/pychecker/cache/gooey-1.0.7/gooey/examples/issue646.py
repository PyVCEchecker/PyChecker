import wx
import sys
import time

from gooey import Gooey, GooeyParser, constants

bg_color = "#000000"
font_color = "#7CFC00"


@Gooey(program_name="This is a cool name")
def gooey_app():
    parser = GooeyParser()

    parser.add_argument('a',
                        metavar='N',
                        type=str,
                        nargs='+',
                        widget='FileChooser')

    parser.add_argument('paths',
                        metavar='N',
                        type=str,
                        nargs='+',
                        widget='MultiFileChooser')
    args = parser.parse_args()

    # Do something for a long time
    print(args)
    print(len(args.paths))
    for i in args.paths:
        print(i)

if __name__ == '__main__':
    sys.exit(gooey_app())



parser.add_argument('paths',
metavar='N',
type=str,
nargs='+',
widget='MultiFileChooser')