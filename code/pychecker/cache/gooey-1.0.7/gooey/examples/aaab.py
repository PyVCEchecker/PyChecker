from gooey import Gooey, GooeyParser, options


# @Gooey(program_name='1.0.7 Demo')
# def main():
#     parser = GooeyParser(description='Some words')
#     parser.add_argument(
#         '--filteroption',
#         help='General text input',
#         metavar='Select Column Name',
#         gooey_options={
#             'placeholder': 'I am a placeholder!',
#             'full_width': True,
#             'show_label': False,
#         }
#     )
#
#     parser.add_argument(
#         '--filteroption2',
#         help='Textareas do it, too',
#         metavar='Select Column Name',
#         widget='Textarea',
#         gooey_options={
#             'placeholder': 'Whoa, Me too!',
#             'full_width': True,
#             'show_label': False
#         }
#     )
#
#     parser.add_argument(
#         '--filteroption3',
#         help='Password fields',
#         metavar='Password',
#         widget='PasswordField',
#         gooey_options={
#             'placeholder': 'Enter a secret here. *****',
#             'full_width': True,
#             'show_label': False
#         }
#     )
#     parser.add_argument(
#         '--filteroption4',
#         help='And all the choosers!',
#         metavar='Password',
#         widget='FileChooser',
#         gooey_options={
#             'placeholder': 'What file you want?',
#             'full_width': True,
#             'show_label': False
#         }
#     )
#     args = parser.parse_args()
#     print(args)


@Gooey(program_name='1.0.7 Demo')
def main():
    parser = GooeyParser(description='Some words')
    parser.add_argument(
        '--integer',
        help='Integer input field',
        metavar='Integers',
        # widget='IntegerField',
        gooey_options=options.IntegerField(
            validator={
                'test': 'int(user_input) < 10',
                'message': 'must be lower than 10!'
            },
            min=0,
            max=10,
            increment=1,
            full_width=True
        )
    )
    parser.add_argument(
        '--decimal',
        help='Decimal input field',
        metavar='Decimals',
        widget='DecimalField',
        gooey_options=options.DecimalField(
            min=0.0,
            max=0.1,
            increment=0.01,
            precision=2,
            full_width=True
        )
    )

    parser.add_argument(
        '--slider',
        help='Slider input field',
        metavar='Integer Slider',
        widget='Slider',
        gooey_options=options.Slider(
            min=0,
            max=1000,
            increment=1,
            full_width=True
        )
    )

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()