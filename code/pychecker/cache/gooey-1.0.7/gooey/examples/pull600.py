from gooey import Gooey, GooeyParser


@Gooey()
def main():
    parser = GooeyParser(add_help=False)
    parser.add_argument('--c_file', widget='FileChooser')

    args = parser.parse_args()

    for i in range(4):
        import time
        # time.sleep(1)
        print('sleeping...', time.time())


if __name__ == '__main__':
    main()



