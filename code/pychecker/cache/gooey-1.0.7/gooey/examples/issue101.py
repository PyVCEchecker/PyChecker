from gooey import Gooey, GooeyParser


@Gooey(program_name="Time Selection", use_cmd_args=True)
def parse_args(default_name):
    parser = GooeyParser(description="Select a time!")
    parser.add_argument('--foo', metavar='Select a Time', help="Time when we should start the program", widget='TimeChooser')

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    conf = parse_args("/sample")
    print("Done")