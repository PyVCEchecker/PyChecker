from gooey import Gooey, GooeyParser


@Gooey
def main():
    parser = GooeyParser()
    parent = parser.add_argument_group('Search Options', gooey_options={
        'columns': 2
    })
    parent.add_argument('--query-string', help='the search string')

    child_one = parent.add_argument_group('flags', gooey_options={'show_border': True})
    child_one.add_argument('--option1', help='some text here')

    child_two = parent.add_argument_group('price', gooey_options={'show_border': True})
    child_two.add_argument('--option2', help='some text here')
    args = parser.parse_args()


if __name__ == '__main__':
    main()