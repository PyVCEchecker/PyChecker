import argparse
from gooey import Gooey, GooeyParser

# @Gooey
def main():
    parser = GooeyParser()
    # parser.add_argument("--enable-foo", action="store_true", help="enable the foo option")
    # parser.add_argument("--disable-bar",action="store_true",  help="disable the bar option", gooey_options={
    #     'show_label': True
    # }# , widget='BlockCheckbox'
    #                     )
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    print(args)


main()





