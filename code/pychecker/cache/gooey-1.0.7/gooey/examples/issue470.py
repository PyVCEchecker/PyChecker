from argparse import *
from pathlib import Path
from gooey import Gooey

@Gooey
def main():
    parser = ArgumentParser()
    parser.add_argument("--foo", type=FileType("r"))
    parser.add_argument("--bar", type=Path)
    print(parser.parse_args())

main()