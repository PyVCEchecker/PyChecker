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


@Gooey(
    program_name='Advanced Layout Groups',
    sidebar_title="Your Custom Title",
    show_sidebar=False,
    dump_build_config=True,
    tabbed_groups=False,
    # body_bg_color='#ffffff'
    menu=[{
        'name': 'File',
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': 'About',
                'name': 'Gooey Layout Demo',
                'description': 'An example of Gooey\'s layout flexibility',
                'version': '1.2.1',
                'copyright': '2018',
                'website': 'https://github.com/chriskiehl/Gooey',
                'developer': 'http://chriskiehl.com/',
                'license': 'MIT'
            }, {
                'type': 'MessageDialog',
                'menuTitle': 'Information',
                'caption': 'My Message',
                'message': 'I am demoing an informational dialog!'
            }, {
                'type': 'Link',
                'menuTitle': 'Visit Our Site',
                'url': 'https://github.com/chriskiehl/Gooey'
            }]
        },{
        'name': 'Help',
        'items': [{
            'type': 'Link',
            'menuTitle': 'Documentation',
            'url': 'https://www.readthedocs.com/foo'
        }]
    }]
)
def main():
    message = (
        'Hi there!\n\n' 
        'Welcome to Gooey! \nThis is a demo of the flexible layouts and overall' 
        'customization you can achieve by using argument groups and '
        'the new gooey_options feature.')



    import sys
    print(sys.argv)
    desc = "Example application to show Gooey's various widgets"
    file_help_msg = "Name of the file you want to process"
    my_cool_parser = GooeyParser(description=desc, add_help=False)

    categories = my_cool_parser.add_argument_group(
        'Example 1',
        description='This is the default group style',
        gooey_options={
            'show_underline': True,
            'show_border': False,
            # 'label_color': '#FF9900',
            'columns': 1,
            # 'margin_top': 90
        }
    )

    categories.add_argument(
        '--subcategoryasdf2asdf',
        metavar='Parent Category',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
    )

    categories.add_argument(
        '--subcategory',
        metavar='Subcategory',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
    )

    categories1 = my_cool_parser.add_argument_group(
        'Example 2',
        description='This is an argument group with no horizontal line break',
        gooey_options={
            'show_underline': False,
            'show_border': False,
        }
    )

    categories1.add_argument(
        '--subcategoryasdf2asdfasdf',
        metavar='Parent Category',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
    )

    categories1.add_argument(
        '--subcategory1',
        metavar='Subcategory',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
    )


    categories2 = my_cool_parser.add_argument_group(
        'Example 3',
        description='This is an argument group with show_border = True',
        gooey_options={
            'show_underline': False,
            'show_border': True,
            # 'label_color': '#FF9900',
            # 'columns': 2,
            # 'margin_top': 90
        }
    )

    categories2.add_argument(
        '--subcategoryasdf2',
        metavar='Parent Category',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
    )

    categories2.add_argument(
        '--subcategory2',
        metavar='Subcategory',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
    )





    my_cool_parser.print_help()
    args = my_cool_parser.parse_args()
    print(args)
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
