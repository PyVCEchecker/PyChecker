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
    program_name='Gooey Demo',
    sidebar_title="Your Custom Title",
    show_sidebar=False,
    dump_build_config=True,
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
    desc = "Gooey transforms your CLI applications into beautiful GUIs!"
    file_help_msg = "Name of the file you want to process"
    my_cool_parser = GooeyParser(description=desc, add_help=False)

    # categories = my_cool_parser.add_argument_group(
    #     'Input Stage',
    #     gooey_options={
    #         'show_border': True,
    #         # 'label_color': '#FF9900',
    #         'columns': 2,
    #         # 'margin_top': 30
    #     }
    # )
    #
    # categories.add_argument(
    #     '--subcategory',
    #     metavar='File',
    #     help='Path the audio file to encode.',
    #     widget='FileChooser',
    #     required=True,
    #     gooey_options={
    #     })
    #
    # categories.add_argument(
    #     '--subcategory21',
    #     metavar='File',
    #     help='Path the audio file to encode.',
    #     widget='FileChooser',
    #     required=True,
    #     gooey_options={
    #     })


    # categories.add_argument(
    #     '--parent-category',
    #     metavar='Bitrate',
    #     help='The constant or variable bitrate (depending on codec choice)',
    #     choices=['a', 'b', 'c'],
    #     required=True,
    #     gooey_options={
    #         'label_color': '#FF9900',
    #         'label_bg_color': '#0000FF',
    #         # 'help_color': '#ff00ff',
    #         'help_bg_color': '#ff00ff'
    #     })



    search_options = my_cool_parser.add_argument_group(
        'Output Stage',
        'Specify the desired output behavior for the encoded file.',
        gooey_options={
            'show_border': True,
            'columns': 2,
            'margin_top': 25
        }
    )

    search_options.add_argument('--query',
                                metavar="Output File",
                                help='The output destination for the encoded file',
                                widget='FileChooser',
                                gooey_options={'full_width': True})
    #
    search_flags = search_options.add_argument_group('Resampling',
                                                     gooey_options={'show_border': True}
                                                     )
    search_flags.add_argument('--buy-it-now',
                              metavar='Lowpass',
                              help="Frequency(kHz), lowpass filter cutoff above freq.",
                              action='store_true',
                              widget='BlockCheckbox',
                              gooey_options={
                                  'checkbox_label': 'Enable'
                              })
    search_flags.add_argument('--auction',
                              metavar='Resample',
                              help="Sampling frequency of output file(kHz)",
                              action='store_true',
                              widget='BlockCheckbox',
                              gooey_options={
                                  'checkbox_label': 'Enable'
                              })

    # price_range = search_options.add_argument_group('Price_Range',
    #                                                 gooey_options={'show_border': True}
    #                                                 )
    #
    # price_range.add_argument('--price-min',
    #                          help='This'
    #                          )
    # price_range.add_argument(
    #     '--price-max',
    #     metavar='Priority',
    #     help='sets the process priority (Windows and OS/2-specific)',
    #     choices=[0,1,2,3,4],
    #     default=2
    # )

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
