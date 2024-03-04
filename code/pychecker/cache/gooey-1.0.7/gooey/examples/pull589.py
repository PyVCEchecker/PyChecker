from gooey import Gooey, GooeyParser
import os

@Gooey(optional_cols=2,
        program_name="Elapsed / Remaining Timer on Progress in Gooey",
        progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
        progress_expr="current / total * 100",
        timing_options = {
                'show_time_remaining':True,
                'hide_time_remaining_on_complete':False
        }
        )
def parse_args():
    prog_descrip = 'Elapsed / Remaining Timer on Progress in Gooey'
    parser = GooeyParser(description=prog_descrip)

    sub_parsers = parser.add_subparsers(help='commands', dest='command')

    range_parser = sub_parsers.add_parser('range')

    range_parser.add_argument('--length',default=10000)

    return parser.parse_args()

def compute_range(length):
    for i in range(10):
        import time
        from random import randint
        time.sleep(.4)
        print(f"progress: {i}/{10}")

if __name__ == '__main__':
    conf = parse_args()
    if conf.command == 'range':
        compute_range(int(conf.length))




# from gooey import Gooey, GooeyParser
# import os
#
#
# @Gooey(progress={
#     'progress_bar': {
#         'regex': r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
#         # could pass the full args namespace here...?
#         # Hmm...
#         'expr': "current / total * 100"
#     },
#     'elapsed': {
#         'show': True,
#         'format': '00:00',
#         'hide_on_completion': False
#     },
#     'estimated_remaining': {
#         'show': True,
#         'format': '00:00',
#         'hide_on_completion': False
#     }
# })
#
#
# @Gooey(optional_cols=2,
#        program_name="Elapsed / Remaining Timer on Progress in Gooey",
#        progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
#        progress_expr="current / total * 100",
#        hide_progress_msg=True,
#        timing={
#            'elapsed': {
#                'show': True,
#                'format': '00:00',
#                'hide_on_completion': False
#            },
#            'estimated_remaining': {
#                'show': True,
#                'format': '00:00',
#                'hide_on_completion': False
#            }
#        }
#        )
# def parse_args():
#     prog_descrip = 'Elapsed / Remaining Timer on Progress in Gooey'
#     parser = GooeyParser(description=prog_descrip)
#
#     sub_parsers = parser.add_subparsers(help='commands', dest='command')
#
#     range_parser = sub_parsers.add_parser('range')
#
#     range_parser.add_argument('--length',default=50)
#
#     return parser.parse_args()
#
# def compute_range(length):
#
#     for i in range(length):
#         import time
#         print('Action 1: expensive computation', str(time.time()))
#         time.sleep(.2)
#         print(f"progress: {i}/{length}")
#
#     for i in range(length):
#         import time
#         print('Action 2: some log about an expensive computation', str(time.time()))
#         time.sleep(.2)
#         print(f"progress: {i}/{length}")
#
# if __name__ == '__main__':
#     conf = parse_args()
#     if conf.command == 'range':
#         compute_range(int(conf.length))