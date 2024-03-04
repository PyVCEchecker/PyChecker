from gooey import Gooey
from gooey import GooeyParser

@Gooey(
    program_name='ICC-OBS Version 0.1',
    show_stop_warning=False,
    force_stop_is_error=False,
    disable_progress_bar_animation=True,
    required_cols=1,
    advanced=True,
    navigation='TABBED',
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
                'menuTitle': 'Get Data',
                'url': 'https://data.ccca.ac.at/group/climaproof'
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
	parser = GooeyParser(description='Example About Dialoge')
	parser.add_argument('filename', help="name of the file to process")
	args = parser.parse_args()

if __name__ == "__main__":
    main()