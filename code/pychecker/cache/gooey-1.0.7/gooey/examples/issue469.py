from argparse import *
from pathlib import Path
from gooey import Gooey

@Gooey(dump_build_config=True)
def main():
    parser = ArgumentParser()
    parser.add_argument("--foo", default=SUPPRESS)
    parser.add_argument('--version', action='version', version='1.0')
    print(parser.parse_args())

main()