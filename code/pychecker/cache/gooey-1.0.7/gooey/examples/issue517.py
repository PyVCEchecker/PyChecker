import os

from gooey import Gooey, GooeyParser

@Gooey()
def main():
    parser = GooeyParser(description='Just display the console')

    parser.add_argument('--host', help='Ze host!', default=os.environ.get('HOST'))
    group = parser.add_mutually_exclusive_group(required=False,
                                                # gooey_options={"initial_selection": 0}
                                                )
    group.add_argument("-b", type=str)
    group.add_argument("-d", type=str, widget="DateChooser")
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()