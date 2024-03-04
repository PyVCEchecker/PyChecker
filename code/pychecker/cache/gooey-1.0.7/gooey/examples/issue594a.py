"""
Demo
"""
import csv
import zipfile
from io import TextIOWrapper

from gooey import Gooey, GooeyParser, PrefixTokenizers, options


print()



with zipfile.ZipFile(r'C:\Users\Chris\Downloads\simplemaps_worldcities_basicv1.71\worldcities.zip') as zf:
    with zf.open('worldcities.csv', 'r') as f:
        reader = csv.reader(TextIOWrapper(f, 'utf-8'))
        data = ['{} - {}'.format(x[4], x[1]) for x in reader][1:][:5000]


@Gooey(program_name='FilterableDropdown Demo', poll_external_updates=True)
def main():
    parser = GooeyParser(description="Example of the Filterable Dropdown")
    parser.add_argument(
        "-a",
        "--myargument",
        metavar='Country',
        help='Search for a country',
        choices=data,
        widget='FilterableDropdown',
        gooey_options=options.FilterableDropdown(**{
            'label_color': (255, 100, 100),
            'placeholder': 'Start typing to view suggestions',
            'search_strategy': options.SearchStrategy(**{
                'type': 'PrefixFilter',
                'choice_tokenizer': PrefixTokenizers.WORDS,
                'input_tokenizer': PrefixTokenizers.REGEX('\s'),
                'ignore_case': True,
                'operator': 'AND',
                'index_suffix': False
            })
        }))
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    import sys
    import json
    if 'gooey-seed-ui' in sys.argv:
        print(json.dumps({'-b': data}))
    else:
        main()
