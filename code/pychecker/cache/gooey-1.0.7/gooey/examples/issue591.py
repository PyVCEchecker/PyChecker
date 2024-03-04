import json
import sys
from pprint import pprint

from gooey import Gooey, GooeyParser


@Gooey(program_name="Using Dynamic Values", poll_external_updates=True)
def main():
    parser = GooeyParser()
    parser.add_argument(
        '--name',
        metavar='name',
        widget='Dropdown',
        choices=[str(i) for i in range(500)]
    )

    args = parser.parse_args()
    pprint(args)


if __name__ == '__main__':
    from random import randint
    if 'gooey-seed-ui' in sys.argv:
        l = [str(i) for i in range(randint(1, 10))]
        print(json.dumps({'--name': l}))
        exit()
    print("-" * 80)
    pprint(sys.argv)
    main()