from gooey import Gooey, GooeyParser


@Gooey(tabbed_groups=True, default_size=(800, 600))
def create_arg_parser():
    arg_parser = GooeyParser()
    group = arg_parser.add_argument_group('Input/Output', gooey_options={'columns': 1})
    group.add_argument(dest='divisions_file', widget='FileChooser', help=(
        'The CSV with division information; see the Division Columns tab for details.'
    ))
    group.add_argument(dest='professors_file', widget='FileChooser',
        help='The CSV with professor information; see Professor Columns tab for details.',
    )
    group.add_argument(dest='students_file', widget='FileChooser',
        help='The CSV with student information; see the Student Columns tab for details.'
    )
    group.add_argument(dest='output_dir', default='~/Desktop/', widget='DirChooser',
        help='The folder to put the output.csv.',
    )
    return arg_parser


def main():
    arg_parser = create_arg_parser()
    arg_parser.parse_args()


if __name__ == '__main__':
    main()