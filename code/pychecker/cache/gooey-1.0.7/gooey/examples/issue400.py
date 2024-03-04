import argparse
from gooey import Gooey, GooeyParser
from examples.issue458.resource import ConstantArray

def get_resource(num):
    return ConstantArray[num]

@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument("FileChooser", widget="FileChooser",
                        gooey_options={
                            'wildcard':
                                "Comma separated file (*.csv)|*.csv|"
                                "All files (*.*)|*.*",
                            'default_dir': "c:/batch",
                            'default_file': "def_file.csv",
                            'message': "pick me"
                        }
                        )
    parser.add_argument("DirectoryChooser", widget="DirChooser",
                        gooey_options={
                            'wildcard':
                                "Comma separated file (*.csv)|*.csv|"
                                "All files (*.*)|*.*",
                            'message': "pick folder",
                            'default_path': r"C:\Users\Chris\Documents\books"
                        }
                        )
    parser.add_argument("FileSaver", widget="FileSaver",
                        gooey_options={
                            'wildcard':
                                "JPG (*.jpg)|*.jpg|"
                                "All files (*.*)|*.*",
                            'message': "pick folder",
                            'default_dir': "c:/projects",
                            'default_file': "def_file.csv"
                        }
                        )
    parser.add_argument("MultiFileSaver", widget="MultiFileChooser",
                        gooey_options={
                            'wildcard':
                                "Comma separated file (*.csv)|*.csv|"
                                "All files (*.*)|*.*",
                            'message': "pick folder",
                            'default_dir': "c:/temp",
                            'default_file': "def_file.csv"
                        }
                        )
    args = parser.parse_args()

    print(get_resource(int(args.ResourceNumber)))

if __name__ == "__main__":
    main()


