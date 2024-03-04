from gooey import Gooey, GooeyParser
from argparse import ArgumentParser

def some_function(id_, len_):
    print(id_)
    print(len_)
    return

@Gooey(program_name = "Machine Learning Pipeline - Spatial Proximity Check", required_cols = 2)
# define main function to execute user based query
def subprocess(args):
    # pop the filename off the sys.argv list
    pipeline_arg = sys.argv.index('--pipeline_dataset')
    pipeline_val = sys.argv[pipeline_arg + 1]
    # feed it to the rest of your program as usual
    # df = pd.read_csv(dataset)
    # cols = tuple(df.columns)

    parser2 = GooeyParser(description = "Machine Learning Pipeline - Base Data Input")
    parser2.add_argument('--pipeline_dataset', widget='Textarea', default=pipeline_val, required=True, gooey_options={'visible': False})
    parser2.add_argument('id', metavar = 'ID Column Name', widget = 'Dropdown', choices = [pipeline_val])
    parser2.add_argument('length', metavar = 'Length (ft) Column Name', widget = 'Dropdown', choices = [pipeline_val])
    args = parser2.parse_args()
    print(args)

import sys
subprocess(sys.argv)