import gooey

@gooey.Gooey(dump_build_config=True)
def main():
    parser = gooey.GooeyParser()

    # parser.add_argument("--test")

    mutex_1 = parser.add_mutually_exclusive_group(required=True)
    mutex_1.add_argument('--choose-1', action='store_true', default=False)
    mutex_1.add_argument('--choose-2', action='store_true', default=False)

    # mutex_2 = parser.add_mutually_exclusive_group(required=True)
    # mutex_2.add_argument('--choose-3', action='store_true', default=False)
    # mutex_2.add_argument('--choose-4', action='store_true', default=False)

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()