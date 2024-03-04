from threading import Thread

from gooey import Gooey, GooeyParser
from argparse import SUPPRESS
import subprocess

cmd = [
    'ffmpeg',
    '-to', '30',
    '-i', 'Castle-in-the-Sky.mkv',
    'Castle-in-the-Sky.mp4'
]

@Gooey
def main():
    parser = GooeyParser()
    # parser.add_argument('filename1')
    args = parser.parse_args()

    process = subprocess.Popen(
        ' '.join(cmd),
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
    main()

