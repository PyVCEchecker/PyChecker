import sys
import time

from gooey import Gooey, GooeyParser


@Gooey(show_stop_warning=False)
def gooey_app():
    parser = GooeyParser()
    args = parser.parse_args()

    # Do something for a long time
    for i in range(100):
        time.sleep(1)

    return 0

if __name__ == '__main__':
    sys.exit(gooey_app())