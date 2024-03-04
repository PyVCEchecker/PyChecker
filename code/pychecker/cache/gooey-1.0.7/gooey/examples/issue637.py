import wx
import sys
import time

from gooey import Gooey, GooeyParser, constants
from gooey.gui.components.widgets.core import TextInput

bg_color = "#000000"
font_color = "#7CFC00"


@Gooey(program_name="This is a cool name")
def gooey_app():
    parser = GooeyParser()

    parser.add_argument('-f', '--foo',
                        help="Hello world!",
                        dest='foobar',
                        metavar='Hello World!',
                        action='count',
                        gooey_options={
        'label_color': '#ffffff'
    })

    parser.add_argument('-f', '--foo',
                        help="Hello world!",
                        dest='foobar',
                        metavar='Hello World!',
                        action='count',
                        widget=TextInput(
                            label_color='#fff',
                            placeholder='One Two Three'
                        ))
    args = parser.parse_args()

    # Do something for a long time
    print(args)

if __name__ == '__main__':
    sys.exit(gooey_app())