import argparse
from gooey import Gooey
from gooey import GooeyParser


class CustomHelpFormatter(argparse.HelpFormatter):

    def _format_action(self, action):
        a = 10
        super(CustomHelpFormatter, self)._format_action(action)






@Gooey(program_name='some program')
def main():
    someparser = argparse.ArgumentParser(description='Some words', formatter_class=CustomHelpFormatter)
    someparser = GooeyParser(description='Some words', formatter_class=CustomHelpFormatter)
    someparsers = someparser.add_subparsers(dest='someplace')
    somesubparser = someparsers.add_parser('someoption')
    croc_facts = somesubparser.add_argument_group(
        'Just Crocodile Things',
        description='There are 13 species of crocodiles, so there are many different ' +
                    'sizes of crocodile. The smallest crocodile is the dwarf crocodile. ' +
                    'It grows to about 5.6 feet (1.7 meters) in length and weighs 13 to 15 pounds ',
        gooey_options={
            'show_border': True,
        }
    )
    someothersubparser = someparsers.add_parser('someotheroption', help='foo')
    someoption = croc_facts.add_argument('-somecrocodile', action='store_true', help='Nothing to see here, move along.')
    someparser.parse_args()


main()