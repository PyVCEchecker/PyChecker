import wx
import sys
import time

from gooey import Gooey, GooeyParser, constants

bg_color = "#000000"
font_color = "#7CFC00"


@Gooey(
    #Background Settings
    # header_bg_color=bg_color,
    # body_bg_color=bg_color,
    # footer_bg_color=bg_color,
    # terminal_panel_color='#ffff00',
    # #Font Settings
    # terminal_font_family='Arial',
    # terminal_font_color=font_color,
    # terminal_font_weight=100
)
def gooey_app():
    parser = GooeyParser()

    parser.add_argument('-f', '--foo', help="Hello world!", gooey_options={
        'label_color': '#ffffff'
    })
    args = parser.parse_args()

    # Do something for a long time
    for i in range(1):
        print(time.time())
        print("HELLOO!!!!")
        time.sleep(1)

    return 0

if __name__ == '__main__':
    sys.exit(gooey_app())