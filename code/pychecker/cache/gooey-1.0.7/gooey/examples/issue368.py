from gooey import Gooey, GooeyParser
import argparse

@Gooey
def main():
    cli = GooeyParser(description='Utils')
    required_args = cli.add_argument_group("Required Arguments")
    required_args.add_argument(
        '-i', '--in', required=True, metavar='PATH', dest='inpath'
    )
    required_args.add_argument(
        '-o', '--out', required=True, metavar='PATH', dest='outpath'
    )

    advanced_section = cli.add_argument_group(
        "Advanced Options",
        description='Change these options at your own risk!!!',
        gooey_options={
            'show_border': True
        }
    )

    advanced_section.add_argument('--dont-destroy-computer',
                                  help='When enabled this will NOT cause an explosion',
                                  metavar="Avoid Violently Delf Destruct",
                                  action='store_true',
                                  widget='BlockCheckbox',
                                  default=True)
    args = cli.parse_args()

if __name__ == '__main__':
    main()