from gooey import Gooey, GooeyParser


@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument('filename1')
    parser.add_argument(
        'secret-advanced-argument',
        default='TOO POWERFUL!!',
        gooey_options={'visible': False}
    )
    args = parser.parse_args()


if __name__ == '__main__':
    main()