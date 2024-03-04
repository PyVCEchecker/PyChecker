import argparse
from gooey import Gooey


@Gooey
def main():
    parser = argparse.ArgumentParser(prog="aria2p")
    subparsers = parser.add_subparsers(dest="subcommand", metavar="", prog="aria2p")
    subcommand_help = "Show this help message and exit."

    def subparser(command, text, **kwargs):
        sub = subparsers.add_parser(command, add_help=False, help=text, description=text, **kwargs)
        sub.add_argument("-h", "--help", action="help", help=subcommand_help)
        return sub

    pause_parser = subparser("pause", "Pause downloads.", aliases=["stop"])

    args = parser.parse_args()

# if __name__ == '__main__':
main()