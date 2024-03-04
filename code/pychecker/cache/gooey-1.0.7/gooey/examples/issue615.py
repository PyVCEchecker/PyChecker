from gooey import Gooey, GooeyParser
from argparse import ArgumentParser

def some_function(id_, len_):
    print(id_)
    print(len_)
    return

@Gooey(program_name = "Machine Learning Pipeline - Spatial Proximity Check",
       required_cols = 2,
       target=r'C:\Users\Chris\Dropbox\pretty_gui\Gooey\gooey\examples\issue615a.py',
       suppress_gooey_flag=True)
def main_spatial_proximity_gui():
    parser = GooeyParser(description = "Machine Learning Pipeline - Base Data Input")
    parser.add_argument('--pipeline_dataset', metavar = 'Pipeline Dataset (csv)', type = str, widget = 'FileChooser')
    args = parser.parse_args()




main_spatial_proximity_gui()
