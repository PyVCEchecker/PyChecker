from gooey import Gooey, GooeyParser

@Gooey()
def main():
    parser = GooeyParser(description='Process some integers.')

    parser.add_argument(
        "--arg1",
        action="store",
        default="c1",
        choices=("c1", "c2", "c3"),
    )

    args = parser.parse_args()


if __name__ == '__main__':
    main()