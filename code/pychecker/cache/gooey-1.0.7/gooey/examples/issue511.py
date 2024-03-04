from gooey import Gooey, GooeyParser


@Gooey(program_name='My Super Awesome Program',
       default_size=(670, 615),
       header_show_title=True,
       dump_build_config=True,
       menu=[{
           'name': 'Help',
           'items': [{
               'type': 'Link',
               'menuTitle': 'Visit Our Site',
               'url': 'https://github.com/chriskiehl/Gooey'
           }]
       }]
       )
def main():
    '''
    Dummy Function to create a gooey GUI and test the issue.
    '''
    parser = GooeyParser(
        description='This is my program.\nThere are many like it, but this one is mine.')
    parser.add_argument('myfolder', widget='DirChooser',
                        help='Path to directory where output will be stored.')
    args = parser.parse_args()

    print('I\'m a dummy!')


main()