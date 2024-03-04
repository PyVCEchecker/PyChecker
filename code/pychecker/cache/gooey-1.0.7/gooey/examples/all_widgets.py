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
    show_sidebar=True,
    dump_build_config=True,
    requires_shell=False,
    about={
        'name': 'Howdy',
        'version': '1.2.1',
        'copyright': '(C) yo mama'
    }
    # language='russian'
)
def main():
    import sys
    print(sys.argv)
    desc = "Example application to show Gooey's various widgets"
    file_help_msg = "Name of the file you want to process"
    parser = GooeyParser(description=desc, add_help=False)

    # parser.add_argument('--textfield', default=2, widget="TextField", gooey_options={'full_width': True})
    # parser.add_argument('--textarea', default="oneline twoline", widget='Textarea')
    # parser.add_argument('--password', default="hunter42", widget='PasswordField')
    # parser.add_argument('--commandfield', default="cmdr", widget='CommandField')
    # parser.add_argument('--dropdown',
    #                     choices=["one", "two"], default="two", widget='Dropdown')
    # parser.add_argument('--listboxie',
    #                 nargs='+',
    #                 default=['Option three', 'Option four'],
    #                 choices=['Option one', 'Option two', 'Option three',
    #                          'Option four'],
    #                 widget='Listbox',
    #                 gooey_options={
    #                     'height': 300,
    #                     'validate': '',
    #                     'heading_color': 'ff0000',
    #                     'text_color': '',
    #                     'hide_heading': False,
    #                     'hide_text': True,
    #                 }
    #             )
    # parser.add_argument('-c', '--counter', default=3, action='count', widget='Counter')
    # #
    # parser.add_argument("-o", "--overwrite", action="store_true",
    #                             default=True,
    #                             widget='CheckBox')
    #
    # ### Mutex Group ###
    # verbosity = parser.add_mutually_exclusive_group(
    #     required=True,
    #     gooey_options={
    #         'initial_selection': 1
    #     }
    # )
    # verbosity.add_argument(
    #     '--mutexone',
    #     default=True,
    #     action='store_true',
    #     help="Show more details")
    #
    # verbosity.add_argument(
    #     '--mutextwo',
    #     default='mut-2',
    #     widget='TextField')

    parser.add_argument("--filechooser", default="fc-value", widget='FileChooser', gooey_options={
        'defaultFile': 'Sup nigga',
        'message': 'Sup fam',
        'wildcard': 'nig juice'
    })
    parser.add_argument("--filesaver", default="fs-value", widget='FileSaver')
    parser.add_argument("--dirchooser", default="dc-value", widget='DirChooser')
    parser.add_argument("--datechooser", default="2015-01-01", widget='DateChooser')
    parser.add_argument("--multifilechooser", default="2015-01-01", widget='MultiFileChooser')
    parser.add_argument("--multidirchooser", default="2015-01-01", widget='MultiDirChooser')


    dest_vars = [
        'textfield',
        'textarea',
        'password',
        'commandfield',
        'dropdown',
        'listboxie',
        'counter',
        'overwrite',
        'mutextwo',
        'filechooser',
        'filesaver',
        'dirchooser',
        'datechooser'

    ]


    args = parser.parse_args()
    for i in dest_vars:
        assert getattr(args, i) is not None
    print("Success")


if __name__ == '__main__':
    main()
