from gooey import Gooey, GooeyParser


@Gooey(program_name="Widget Demo")
def main():
    my_cool_parser = GooeyParser()

    my_cool_parser.add_argument('--No', choices=[True, False], default=True)
    my_cool_parser.add_argument('--Yes', choices=[True, False], default=False)

    args = my_cool_parser.parse_args()


if __name__ == '__main__':
    main()