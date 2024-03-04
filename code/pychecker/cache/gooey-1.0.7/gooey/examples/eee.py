'''
Created on Dec 21, 2013
 __          __  _
 \ \        / / | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \
    \  /\  /  __/ | (_| (_) | | | | | |  __/
  ___\/__\/ \___|_|\___\___/|_| |_| |_|\___|
 |__   __|
    | | ___
    | |/ _ \
    | | (_) |
   _|_|\___/                    _ _
  / ____|                      | | |
 | |  __  ___   ___   ___ _   _| | |
 | | |_ |/ _ \ / _ \ / _ \ | | | | |
 | |__| | (_) | (_) |  __/ |_| |_|_|
  \_____|\___/ \___/ \___|\__, (_|_)
                           __/ |
                          |___/

@author: Chris
'''

from gooey.python_bindings.gooey_decorator import Gooey
from gooey.python_bindings.gooey_parser import GooeyParser



long_intro = '''
Guess again. And remember, don't do anything that affects anything, unless it turns out you were supposed to, in which case, for the love of God, don't not do it! Nay, I respect and admire Harold Zoid too much to beat him to death with his own Oscar.

Bender?! You stole the atom. Noooooo! Ah, computer dating. It's like pimping, but you rarely have to use the phrase "upside your head." The alien mothership is in orbit here. If we can hit that bullseye, the rest of the dominoes will fall like a house of cards. Checkmate.

That's the ONLY thing about being a slave. Ooh, name it after me! You're going back for the Countess, aren't you? Ooh, name it after me! We don't have a brig. I had more, but you go ahead.

Say it in Russian! You guys go on without me! I'm going to go… look for more stuff to steal! Bite my shiny metal ass. Yeah, lots of people did.
'''

@Gooey(
    program_name='Advanced Layout Groups',
    sidebar_title="Your Custom Title",
    show_sidebar=False,
    dump_build_config=True,
    tabbed_groups=True,
)
def main():
    import sys
    print(sys.argv)
    my_cool_parser = GooeyParser(description='Hai', add_help=False)

    description_area = my_cool_parser.add_argument_group(
        "Introduction",
        long_intro,
        gooey_options={
            'show_border': False,
            'show_underline': False,
        }
    )

    # We need at least on
    description_area.add_argument(
        '-nothing',
        gooey_options={
            'visible': False,
        }
    )

    categories = my_cool_parser.add_argument_group(
        'Categories',
        description='There are 13 species of crocodiles, so there are many different ' +
                    'sizes of crocodile. The smallest crocodile is the dwarf crocodile. ' +
                    'It grows to about 5.6 feet (1.7 meters) in length and weighs 13 to 15 pounds ',
        gooey_options={
            'show_border': False,
            'label_color': '#FF9900',
            'columns': 2,
            # 'margin_top': 90
        }
    )

    categories.add_argument(
        '--parent-category',
        metavar='Parent Category',
        help='This is a very, very, very long help text '
                             'to explain a very, very, very important input value. '
                             'Unfortunately, the end of this long message is cropped. ',
        choices=['a', 'b', 'c'],
        required=True)

    args = my_cool_parser.parse_args()
    print("Hiya!")


if __name__ == '__main__':
    main()
