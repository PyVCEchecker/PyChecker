from gooey import Gooey, GooeyParser


@Gooey(language='chinese')
def main():
    parser = GooeyParser()
    parser.add_argument('filename1')
    parser.add_argument('filename2')
    parser.add_argument('-f', '--foobar')
    args = parser.parse_args()


if __name__ == '__main__':
    main()