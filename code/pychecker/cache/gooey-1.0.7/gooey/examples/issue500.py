import argparse
from gooey import GooeyParser

def get_parser() -> argparse.ArgumentParser:
    parser = GooeyParser()
    parser.add_argument(
        nargs="*",
        default=["foo bar"],
        dest="multi_arg",
    )
    parser.add_argument('--foo', nargs=1, default=['a', 'b'])
    # parser.add_argument(
    #     '--bar',
    #     nargs='+',
    #     choices=["one", "two"],
    #     default="one",
    # )
    parser.add_argument('--listboxie',
                    metavar='Multiple selection',
                    nargs='+',
                    # default=['Option three', 'Option four'],
                    default='123',
                    choices=[123, 'Option two', 'Option three',
                             'Option four'],
                    help='Choose an action!',
                    widget='Listbox',
                    gooey_options={
                        # 'height': 500,
                        'validate': '',
                        'heading_color': '',
                        'text_color': '',
                        'show_label': False,
                        'hide_text': True,
                    }
                    )
    return parser


from gooey import GooeyParser, Gooey
@Gooey
def main():
    args = get_parser().parse_args()
    print(args)
    assert args.multi_arg == ["foo bar"]


if __name__ == "__main__":
    main()