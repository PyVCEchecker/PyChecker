import gooey


@gooey.Gooey
def main():
    parser = gooey.GooeyParser()
    parser.add_argument('--test', default=0, type=int, choices=[0, 1, 2, 3, 4],
                        help='This is a very, very, very long help text '
                             'to explain a very, very, very important input value. '
                             'Unfortunately, the end of this long message is cropped. ')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()