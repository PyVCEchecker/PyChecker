import sys
from pprint import pprint

from gooey import Gooey, GooeyParser

@Gooey( program_name="Using Dynamic Values")
def main():
    parser = GooeyParser()

    g = parser.add_argument_group()

    stuff = g.add_mutually_exclusive_group(
        required=True,
        gooey_options={
            'initial_selection': 0
        }
    )
    stuff.add_argument(
        '--one',
        action='store',
        # gooey_options={
        #     'validator': {
        #         'test': 'user_input',
        #         'message': 'You must supply a value when this option is selected!'
        #     }
        # }
    )
    stuff.add_argument(
        '--two',
        action='store'
    )

    args = parser.parse_args()
    pprint(args)

if __name__ == '__main__':
    print("-"*80)
    pprint(sys.argv)
    main()