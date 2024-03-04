import subprocess

from gooey import GooeyParser, Gooey
from gui.components.options import options

positions = {
    'Center': 'overlay=(W-w)/2:(H-h)/2',
    'Top Left': 'overlay=5:5',
    'Top Right': 'overlay=W-w-5:5',
    'Bottom Left': 'overlay=5:H-h-5',
    'Bottom Right': 'overlay=W-w-5:H-h-5',
}

@Gooey(program_name='Visual FFMPEG')
def version1():
    parser = GooeyParser(description='Visual FFMPEG')
    start_position = parser.add_mutually_exclusive_group(
        'foo',
        gooey_options=options.MutexGroup(
            initial_selection=0,
            full_width=True

        ))
    start_position.add_argument(
        '--ss',
        metavar='All screens',
        help='Records ALL the screens available',
        action='store_true')
    start_position.add_argument(
        '--sss',
        help='start-position as a concrete timestamp',
        gooey_options=options.TextField(
            placeholder='HH:MM:SS',
            validator=options.RegexValidator(
                test='^\d{2}:\d{2}:\d{2}$',
                message='Must be in the format HH:MM:SS'
            )
        ))
    # input_group = parser.add_argument_group('Input', gooey_options=options.ArgumentGroup(
    #     show_border=True
    # ))
    # # basic details
    parser.add_argument(
        '--input',
        help='The video you want to add a watermark to',
        # default=r'C:\Users\Chris\Desktop\Recording #1.mp4',
        widget='TextField',
        gooey_options=options.TextField(
            placeholder='Hello world!',
            wildcard='video files (*.mp4)|*.mp4',
            full_width=True,
            validator={
                'type': 'RegexValidator',
                'test': '^\d{2}:\d{2}:\d{2}$',
                'message': 'you fucked up!'
            })
    )
    # input_group.add_argument(
    #     'watermark',
    #     help='The watermark',
    #     default=r'C:\Users\Chris\Desktop\avatar.png',
    #     widget='FileChooser',
    #     gooey_options=options.FileChooser(
    #         wildcard='PNG files (*.png)|*.png|JPEG files (*.jpeg;*.jpg)|*.jpeg;*.jpg|BMP and GIF files (*.bmp;*.gif)|*.bmp;*.gif',
    #         full_width=True
    #     ))
    #
    # output_group = parser.add_argument_group('Output', gooey_options=options.ArgumentGroup(
    #     show_border=True
    # ))
    # output_group.add_argument(
    #     'output',
    #     help='Choose where to save the output video',
    #     default=r'C:\Users\Chris\Desktop\output.mp4',
    #     widget='FileSaver',
    #     gooey_options=options.FileSaver(
    #         wildcard='video files (*.mp4)|*.mp4',
    #         default_file='output.mp4',
    #         full_width=True
    #     ))
    #
    # output_group.add_argument(
    #     '--overwrite',
    #     metavar='Overwrite existing',
    #     help='Overwrite the output video if it already exists?',
    #     action='store_const',
    #     default=True,
    #     const='-y',
    #     widget='CheckBox')
    #
    # settings = parser.add_argument_group('Settings', gooey_options=options.ArgumentGroup(
    #     show_border=True
    # ))
    # settings.add_argument(
    #     '--opacity',
    #     type=float,
    #     default=75,
    #     widget='Slider',
    #     help='Choose the opacity of the watermark (0-100)', gooey_options=options.DecimalField(
    #         min=0,
    #         max=100,
    #         increment_size=1,
    #     ))
    # settings.add_argument(
    #     '--position',
    #     choices=list(positions.keys()),
    #     default='Center',
    #     help='Position of the watermark')
    args = parser.parse_args()
    print(args)

    cmd_template = 'ffmpeg -i "{input}" ' \
                   '-i "{watermark}" ' \
                   '{overwrite} ' \
                   '-filter_complex "[1]format=rgba,colorchannelmixer=aa={opacity}[logo];[0][logo]{overlay}" ' \
                   '-codec:a copy "{output}"'

    final_cmd = cmd_template.format(
        input=args.input,
        watermark=args.watermark,
        opacity=args.opacity / 100.0,
        overlay=positions[args.position],
        overwrite=args.overwrite,
        output=args.output
    )

    process = subprocess.Popen(
        final_cmd,
        bufsize=1,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        shell=True
    )
    for line in process.stdout:
        print(line)

if __name__ == '__main__':
    version1()