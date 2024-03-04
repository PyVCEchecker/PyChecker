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

from argparse import ArgumentParser
from collections import OrderedDict

from gooey.python_bindings.gooey_decorator import Gooey
from gooey.python_bindings.gooey_parser import GooeyParser






@Gooey(
    sidebar_title="Your Custom Title",
    show_sidebar=False,
    tabbed_groups=False,
    dump_build_config=False,
    required_cols=3,
    optional_cols=1,
    requires_shell=True
)
def main():

    import sys
    print("sys.argv sys.argv sys.argv sys.argv sys.argv sys.argv")
    print(sys.argv)
    print('\n\n')
    print(repr(sys.argv))
    desc = "Example application to show Gooey's various widgets"
    file_help_msg = "Name of the file you want to process"
    my_cool_parser = GooeyParser(description=desc, add_help=False)

    my_cool_parser.add_argument('thing', default='.',
                                widget='MultiFileChooser',
                                help="asdfsadfasdfa sdfadf ad")
    # my_cool_parser.add_argument(
    #     "region_name_list",
    #     help="Which regions do you want to run it for?",
    #     choices=['one' ,'two', 'three'],
    #     nargs="+",
    #     widget="Listbox",
    #     # widget='Counter'
    # )

    my_cool_parser.add_argument("FileChooser",
                    help=file_help_msg,
                    )

    my_cool_parser.add_argument("Outfile",
                                widget='FileChooser',
                                metavar='Output Target',
                                help='Target output file',
                                gooey_options={
                                    'wildcard': 'Some Files (*.png)|*.png',
                                    'label_color': 1234

                                }
                                # gooey_options={
                                #     'validator': {
                                #         'test': 'user_input == "foo"',
                                #         'message': 'Must be a valid filename'
                                #     }
                                # }
                                )
    my_cool_parser.add_argument('--listboxie',
                    metavar='Multiple selection',
                    nargs='+',
                    default=['Option three', 'Option four'],
                    choices=['Option one', 'Option two', 'Option three',
                             'Option four'],
                    help='Choose an action!',
                    widget='Listbox',
                    gooey_options={
                        'height': 500,
                        'validate': '',
                        'heading_color': '',
                        'text_color': '',
                        'hide_heading': True,
                        'hide_text': True,
                    }
                    )
    #
    search_options = my_cool_parser.add_argument_group(
        'Search Options', 'Customize the search options',
        gooey_options={
            'show_border': True,
            'columns': 2
        }
    )

    x = search_options.add_argument('--query', help='base search string'
                                    # , gooey_options={'full_width': True}
                                    )
    search_options.add_argument('--other', help='Another option in the search group'
                                # , gooey_options={'full_width': True}
                                )
    search_options.add_argument('--one-more', help='And another one'
                                # , gooey_options={'full_width': True}
                                )

    search_flags = search_options.add_argument_group('Flags',
                                                     gooey_options={'show_border': True}
                                                     )
    search_flags.add_argument('--buy-it-now', help="Will immediately purchase if possible", action='store_true')
    search_flags.add_argument('--auction', help="Place bids up to PRICE_MAX", action='store_true')

    price_range = search_options.add_argument_group('Price_Range',
                                                    gooey_options={'show_border': True}
                                                    )

    price_range.add_argument('--price-min', help='min price')
    price_range.add_argument('--price-max', help='max price')

    foobar = search_options.add_mutually_exclusive_group(
        gooey_options={'title': 'Numeric Mutexes',
                       'show_border': False,
                       'label_color': '#00ff00'}
    )
    foobar.add_argument('--one', help='oneie')
    foobar.add_argument('--two', help='twoie')
    foobar.add_argument('--three', help='twoie', action='store_true')

    my_cool_parser.add_argument("DirChooser", help=file_help_msg, widget="DirChooser")
    my_cool_parser.add_argument("FileSaver", help=file_help_msg, widget="FileSaver")
    my_cool_parser.add_argument("MultiFileSaver", help=file_help_msg, widget="MultiFileChooser")
    # my_cool_parser.add_argument("MultiDirSaver", help="Directories to open", widget='MultiDirChooser')

    my_cool_parser.add_argument('-j', '--jaws', help='ooop',
                                widget="MultiFileChooser",
                                default="Yo yo!",
                                gooey_options={
                                    'validator': {
                                        'test': 'len(user_input) > 5',
                                        'message': 'Must be over 5 chars!'
                                    }
                                }
                                )
    my_cool_parser.add_argument('-d', '--duration', default=2, type=int,
                                help='Duration (in seconds) of the program output')
    my_cool_parser.add_argument('-u', '--textarea', default="I'm on \na new line",
                                type=str, help='A multiline textarea',
                                widget='Textarea',
                                gooey_options={
                                    'height': 100
                                }
                                )
    my_cool_parser.add_argument('-s', '--cron-schedule', type=int,
                                help='datetime when the cron should begin',
                                widget='DateChooser')
    my_cool_parser.add_argument("-c", "--showtime", action="store_true",
                                help="display the countdown timer")
    my_cool_parser.add_argument("-y", "--yolo", action="store_true",
                                widget='BlockCheckbox',
                                help="display the countdown timer")
    my_cool_parser.add_argument("-p", "--pause", action="store_true",
                                help="Pause execution")
    my_cool_parser.add_argument('-v', '--verbose', action='count')
    my_cool_parser.add_argument("-o", "--overwrite", action="store_true",
                                default=True,
                                help="Overwrite output file (if present)")
    my_cool_parser.add_argument('-r', '--recursive', choices=['yes', 'no'],
                                help='Recurse into subfolders')
    # my_cool_parser.add_argument('-y', '--listboxie',
    #                             nargs='+',
    #                             choices=['hello', 'ay', 'yeah', 'boiiiii', 'wssup', 'longest', 'yeahhhboiii', 'ever'],
    #                             help='Recurse into subfolders',
    #                             widget='Listbox')
    my_cool_parser.add_argument("-w", "--writelog", default="writelogs",
                                help="Dump output to local file")
    my_cool_parser.add_argument("-e", "--error", action="store_true",
                                help="Stop process on error (default: No)")
    verbosity = my_cool_parser.add_mutually_exclusive_group(required=False)
    verbosity.add_argument('-t', '--verbozze', dest='verbose', action='store_true',
                           help="Show more details")
    verbosity.add_argument('-q', '--quiet', dest='quiet',
                           help="Only output on error",
                           # widget='DirChooser'
                           )

    # my_cool_parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    import pprint



    # stuff = [extract(x) for x in my_cool_parser._action_groups]
    # mutex_groups = [group for group in my_cool_parser._mutually_exclusive_groups]
    #
    # pprint.pprint(reapply_mutex_groups(mutex_groups, stuff))
    # my_cool_parser.print_help()
    args = my_cool_parser.parse_args()
    print(args)
    # time.sleep(5)
    print("Hiya!")
    for i in range(20):
        import time
        print('Howdy', i)
        time.sleep(.3)
    # print(args.listboxie)


def here_is_smore():
    pass


if __name__ == '__main__':
    main()
