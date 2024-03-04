import argparse
from gooey import Gooey

class ArgumentHandler:

    def __init__( self, progname ):
        args = self.parser( progname )
        print(args)

    @Gooey
    def parser( self, progname ):
        # Initialize the parser
        parser = argparse.ArgumentParser(prog = progname, description = 'hai')

        # Arguments list
        parser.add_argument( '-x', '--file', help='Some field')

        args = parser.parse_args()

        return args

if __name__ == '__main__':
    ArgumentHandler("foo")