import sys
from gooey import GooeyParser as ArgumentParser
from gooey import Gooey


@Gooey(terminal_font_family="Courier New")
def set_gooey():
    return


def main():
    # If no args were given, display the GUI by calling a decorated function
    if len(sys.argv) == 1:
        set_gooey()

    # Parse command line arguments
    parser = ArgumentParser(description='Testing Gooey DirChooser.')
    parser.add_argument("path", widget="DirChooser",
                        help="Directory.")
    args = parser.parse_args()

    print ("Done")


if __name__ == '__main__':
    main()