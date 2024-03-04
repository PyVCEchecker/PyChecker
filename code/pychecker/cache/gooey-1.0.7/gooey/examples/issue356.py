from gooey import Gooey, GooeyParser, gui


@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument(
        "some_string",
        action="store",
        default="just press Start",
    )

    parser.add_argument(
        '--filteroption', choices=['sku', 'foo', 'bar'],
        help='Select the column name you want to filter data for:',
        widget='Listbox',
        required=True,
        nargs='*',
        metavar='Select Column Name',
        # default='sku'
    )
    parser.add_argument(
        '--filteroption2', choices=['sku', 'foo', 'bar'],
        help='Select the column name you want to filter data for:',
        widget='Listbox',
        required=True,
        nargs='*',
        metavar='Select Column Name',
        default='sku'
    )

    parser.add_argument(
        '--filteroption3', choices=['sku', 'foo', 'bar'],
        help='Select the column name you want to filter data for:',
        widget='Listbox',
        required=True,
        nargs='*',
        metavar='Select Column Name',
        default=['bar']
    )

    parser.add_argument(
        '--filteroption4', choices=['sku', 'foo', 'bar'],
        help='Select the column name you want to filter data for:',
        widget='Listbox',
        required=True,
        nargs='*',
        metavar='Select Column Name',
        default=['sku', 'foo']
    )

    parser.add_argument(
        '--dropdown1', choices=['sku', 'foo', 'bar'],
        help='Select the column name you want to filter data for:',
        required=True,
        nargs='*',
        metavar='Select Column Name',
    )

    parser.add_argument(
        '--dropdown2', choices=['sku', 'foo', 'bar'],
        help='Select the column name you want to filter data for:',
        required=True,
        nargs='*',
        metavar='Select Column Name',
        default='bar'
    )

    args = parser.parse_args()
    print(args, flush=True)

    # print too many messages (causes crash for me around 105k).
    for i in range(2):
        import time
        # time.sleep(.00001)
        print(i)


if __name__ == "__main__":
    main()