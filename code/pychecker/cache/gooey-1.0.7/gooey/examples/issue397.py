from gooey import Gooey, GooeyParser


@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument('numbersonly',
    action='store',
    gooey_options={
        'validator':{
            'test': "re.search(r'[\d]+', user_input)",
            'message': 'must be a number!'
        }
    })
    args = parser.parse_args()


if __name__ == '__main__':
    main()