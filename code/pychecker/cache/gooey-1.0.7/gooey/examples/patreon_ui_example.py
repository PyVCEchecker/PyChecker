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
import csv
import zipfile
from io import TextIOWrapper

from gooey.python_bindings.gooey_decorator import Gooey
from gooey.python_bindings.gooey_parser import GooeyParser

with zipfile.ZipFile(
        r'C:\Users\Chris\Downloads\simplemaps_worldcities_basicv1.71\worldcities.zip') as zf:
    with zf.open('worldcities.csv', 'r') as f:
        reader = csv.reader(TextIOWrapper(f, 'utf-8'))
        locations = ['{} - {}'.format(x[4], x[1]) for x in reader][1:][:5000]


# locations = ["Alabama", "Alaska", '...', "Wyoming"]

@Gooey(program_name='Square BnB')
def version1():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')
    # basic details
    parser.add_argument('location', choices=locations, help='Where are you going?')
    parser.add_argument('check-in', help='Add Dates')
    parser.add_argument('check-out', help='Add Dates')
    parser.add_argument('guests', help='Add Guests')

    # pricing
    parser.add_argument('--min-price', help='Minimum Price')
    parser.add_argument('--max-price', help='Minimum Price')

    # popular filters
    parser.add_argument('--rooms', help='How many rooms do you need?')
    parser.add_argument('--beds', help='How many beds do you need?')
    parser.add_argument('--bathrooms', help='How many bathrooms do you need?')
    parser.add_argument('--entire-place', action='store_true',
                        help='Have the whole place to yourself')
    parser.add_argument('--house', action='store_true', help='No apartments, plz')
    parser.add_argument('--wifi', action='store_true', help='Internet is a must!')
    parser.add_argument('--kitchen', action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


@Gooey(program_name='Square BnB v2.0')
def version2():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    location.add_argument('location', choices=locations, help='Where are you going?')
    location.add_argument('check-in', help='Add Dates')
    location.add_argument('check-out', help='Add Dates')
    location.add_argument('guests', help='Add Guests')

    # pricing
    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument('--min-price', help='Minimum Price')
    pricing.add_argument('--max-price', help='Minimum Price')

    # popular filters
    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True
    })
    filters.add_argument('--rooms', help='How many rooms do you need?')
    filters.add_argument('--beds', help='How many beds do you need?')
    filters.add_argument('--bathrooms', help='How many bathrooms do you need?')
    filters.add_argument('--entire-place', action='store_true',
                         help='Have the whole place to yourself')
    filters.add_argument('--house', action='store_true', help='No apartments, plz')
    filters.add_argument('--wifi', action='store_true', help='Internet is a must!')
    filters.add_argument('--kitchen', action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


@Gooey(program_name='Square BnB v3.0')
def version3():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    # updated!
    location.add_argument('location', choices=locations, help='Where are you going?',
                          gooey_options={
                              'full_width': True
                          })
    # updated!
    location.add_argument('guests', help='Add Guests', gooey_options={'full_width': True})
    location.add_argument('check-in', help='Add Dates')
    location.add_argument('check-out', help='Add Dates')

    # pricing
    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument('--min-price', help='Minimum Price')
    pricing.add_argument('--max-price', help='Minimum Price')

    # popular filters
    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True
    })
    filters.add_argument('--rooms', help='How many rooms do you need?')
    filters.add_argument('--beds', help='How many beds do you need?')
    filters.add_argument('--bathrooms', help='How many bathrooms do you need?')
    filters.add_argument('--entire-place', action='store_true',
                         help='Have the whole place to yourself')
    filters.add_argument('--house', action='store_true', help='No apartments, plz')
    filters.add_argument('--wifi', action='store_true', help='Internet is a must!')
    filters.add_argument('--kitchen', action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


@Gooey(program_name='Square BnB v4.0')
def version4():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    location.add_argument('location', choices=locations, help='Where are you going?',
                          gooey_options={
                              'full_width': True
                          })
    location.add_argument('guests', help='Add Guests', gooey_options={'full_width': True})
    location.add_argument('check-in', help='Add Dates')
    location.add_argument('check-out', help='Add Dates')

    # pricing
    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument('--min-price', help='Minimum Price')
    pricing.add_argument('--max-price', help='Minimum Price')

    # popular filters
    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True,
    })
    # 0. new! This is required to get the group to display..
    filters.add_argument('--ignore-me', gooey_options={'visible': False})
    # 1. new!
    housing = filters.add_argument_group('Rooms and Beds', gooey_options={
        'show_border': True,
        # 2. puts all children in a single column
        'columns': 1
    })
    # 3. updated!
    housing.add_argument('--rooms', help='How many rooms do you need?')
    housing.add_argument('--beds', help='How many beds do you need?')
    housing.add_argument('--bathrooms', help='How many bathrooms do you need?')

    # 4. new!
    ammenities = filters.add_argument_group('Amenities', gooey_options={
        'show_border': True,
        # 5. 2 cols for the checkboxes
        'columns': 2
    })
    # updated!
    ammenities.add_argument('--entire-place', action='store_true',
                            help='Have the whole place to yourself')
    ammenities.add_argument('--house', action='store_true', help='No apartments, plz')
    ammenities.add_argument('--wifi', action='store_true', help='Internet is a must!')
    ammenities.add_argument('--kitchen', action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


@Gooey(program_name='Square BnB v5.0')
def version5():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    location.add_argument(
        'location',
        choices=locations,
        help='Where are you going?',
        widget='FilterableDropdown',
        gooey_options={
            'full_width': True
        })
    location.add_argument('guests', help='Add Guests', gooey_options={'full_width': True})
    location.add_argument('check-in', help='Add Dates')
    location.add_argument('check-out', help='Add Dates')

    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument('--min-price', help='Minimum Price')
    pricing.add_argument('--max-price', help='Minimum Price')

    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True,
    })
    filters.add_argument('--ignore-me', gooey_options={'visible': False})
    housing = filters.add_argument_group('Rooms and Beds', gooey_options={
        'show_border': True,
        # 2. puts all children in a single column
        'columns': 1
    })
    housing.add_argument('--rooms', help='How many rooms do you need?')
    housing.add_argument('--beds', help='How many beds do you need?')
    housing.add_argument('--bathrooms', help='How many bathrooms do you need?')

    ammenities = filters.add_argument_group('Amenities', gooey_options={
        'show_border': True,
        # 5. 2 cols for the checkboxes
        'columns': 2
    })
    ammenities.add_argument('--entire-place', action='store_true',
                            help='Have the whole place to yourself')
    ammenities.add_argument('--house', action='store_true', help='No apartments, plz')
    ammenities.add_argument('--wifi', action='store_true', help='Internet is a must!')
    ammenities.add_argument('--kitchen', action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


@Gooey(program_name='Square BnB v6.0')
def version6():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    location.add_argument(
        'location',
        choices=locations,
        help='Where are you going?',
        widget='FilterableDropdown',
        gooey_options={
            'full_width': True
        })
    location.add_argument(
        'guests',
        help='Add Guests',
        choices=range(11),
        gooey_options={'full_width': True})
    location.add_argument(
        'check-in',
        metavar='Check in',
        widget='DateChooser',
        help='Add Dates')
    location.add_argument(
        'check-out',
        metavar='Check out',
        widget='DateChooser',
        help='Add Dates')

    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument('--min-price', help='Minimum Price')
    pricing.add_argument('--max-price', help='Minimum Price')

    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True,
    })
    filters.add_argument('--ignore-me', gooey_options={'visible': False})
    housing = filters.add_argument_group('Rooms and Beds', gooey_options={
        'show_border': True,
        # 2. puts all children in a single column
        'columns': 1
    })
    housing.add_argument('--rooms', choices=range(11), help='How many rooms do you need?')
    housing.add_argument('--beds', choices=range(11), help='How many beds do you need?')
    housing.add_argument('--bathrooms', choices=range(11), help='How many bathrooms do you need?')

    ammenities = filters.add_argument_group('Amenities', gooey_options={
        'show_border': True,
        # 5. 2 cols for the checkboxes
        'columns': 2
    })
    ammenities.add_argument('--entire-place', action='store_true',
                            help='Have the whole place to yourself')
    ammenities.add_argument('--house', action='store_true', help='No apartments, plz')
    ammenities.add_argument('--wifi', action='store_true', help='Internet is a must!')
    ammenities.add_argument('--kitchen', action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


@Gooey(program_name='Square BnB v8.0')
def version8():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    location.add_argument(
        'location',
        metavar='Location',
        choices=locations,
        help='Where are you going?',
        widget='FilterableDropdown',
        gooey_options={
            'full_width': True
        })
    location.add_argument(
        'guests',
        metavar='Guests',
        help='Add Guests',
        choices=range(11),
        gooey_options={'full_width': True})
    location.add_argument(
        'check-in',
        metavar='Check in',
        widget='DateChooser',
        help='Add Dates')
    location.add_argument(
        'check-out',
        metavar='Check out',
        widget='DateChooser',
        help='Add Dates')

    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument(
        '--min-price',
        help='Minimum Price',
        gooey_options={'show_help': False, 'label_color': '#2e2424'})
    pricing.add_argument(
        '--max-price',
        help='Maximum Price',
        gooey_options={'show_help': False, 'label_color': 1234})

    # FILTERS
    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True,
    })
    filters.add_argument('--ignore-me', gooey_options={'visible': False})
    housing = filters.add_argument_group('Rooms and Beds', gooey_options={
        'show_border': True,
        'columns': 1
    })
    housing.add_argument(
        '--rooms',
        metavar='Rooms',
        choices=range(11), help='How many rooms do you need?')
    housing.add_argument(
        '--beds',
        metavar='Beds',
        choices=range(11), help='How many beds do you need?')
    housing.add_argument(
        '--bathrooms',
        metavar='Bathrooms',
        choices=range(11), help='How many bathrooms do you need?')

    ammenities = filters.add_argument_group('Amenities', gooey_options={
        'show_border': True,
        'columns': 2
    })
    ammenities.add_argument(
        '--entire-place',
        metavar='Entire Place',
        action='store_true',
        help='Have the whole place to yourself')
    ammenities.add_argument(
        '--house',
        metavar='House',
        action='store_true', help='No apartments, plz')
    ammenities.add_argument(
        '--wifi',
        metavar='WIFI',
        action='store_true', help='Internet is a must!')
    ammenities.add_argument(
        '--kitchen',
        metavar='Kitchen',
        action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program


if __name__ == '__main__':
    # version1()
    # version2()
    # version3()
    # version4()
    # version5()
    # version6()
    # version7()
    version8()

"""
search_options = parser.add_argument_group(
        'Search Options',
        'Customize the search options',
        gooey_options={
            'show_border': True,
            'columns': 2,
            'margin_top': 25
        }
    )

    search_options.add_argument('--query', help='base search string'
                                    , gooey_options={'full_width': True}
                                    )
    #
    search_flags = search_options.add_argument_group('Flags',
                                                     gooey_options={'show_border': False}
                                                     )
    search_flags.add_argument('--buy-it-now',
                              metavar='Buy it Now',
                              help="Will immediately purchase if possible",
                              action='store_true',
                              widget='BlockCheckbox',
                              gooey_options={
                                  'label_color': '#4B5F83',
                                  'checkbox_label': 'Enable'
                              })
    search_flags.add_argument('--auction',
                              metavar='Auction',
                              help="Place bids up to PRICE_MAX",
                              action='store_true',
                              widget='BlockCheckbox',
                              gooey_options={
                                  'label_color': '#4B5F83',
                                  'checkbox_label': 'Enable'
                              })

    price_range = search_options.add_argument_group('Price_Range',
                                                    gooey_options={'show_border': True}
                                                    )

    price_range.add_argument('--price-min',
                             help=
                             'This'
                             # 'is a very, very, very long help text '
                             # 'to explain a very, very, very important input value. '
                             )
    price_range.add_argument('--price-max', help='max price')

    args = parser.parse_args()
    print(args)
    print("Hiya!")
    for i in range(20):
        import time
        print('Howdy', i)
        time.sleep(.3)
    # print(args.listboxie)

"""
