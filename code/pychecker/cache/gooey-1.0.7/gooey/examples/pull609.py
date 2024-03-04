from gooey import Gooey, GooeyParser


@Gooey(program_name="Widget Demo")
def main():
    parent = GooeyParser()
    group = parent.add_mutually_exclusive_group('mutex-group')
    group.add_argument("--a_file", widget="FileChooser")
    group.add_argument("--b_file", widget="DirChooser")

    parser = GooeyParser(parents=[parent], add_help=False)
    parser.add_argument('--c_file', widget='FileChooser')


    args = parser.parse_args()


if __name__ == '__main__':
    main()



