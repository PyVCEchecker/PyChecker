from gooey import Gooey, GooeyParser


@Gooey(program_name="Gooey!")
def parse_args(default_name):
    # import sys
    # print(sys.argv)
    parser = GooeyParser(prog="Gooey", description="Gooey turns your CLI apps into beautiful GUIs!")
    parser.add_argument('data_directory',
                        action='store',
                        default='scale=',
                        type=lambda x: 'foo ' + x,
                        widget='DirChooser',
                        # gooey_options={
                        #     'validator': {
                        #         'test': "__import__('re').search('\d+x\d+', user_input) != None",
                        #         'message': 'oops'
                        #     }
                        # }
                        )
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    conf = parse_args("/sample")
    print("Done")