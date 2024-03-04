
from gooey import Gooey, GooeyParser
import sys
import time

@Gooey(progress_regex=r"^(?P<current>\d+)/(?P<total>\d+)$",
       progress_expr="current / total * 100")
def main():
    parser = GooeyParser(prog="example_progress_bar_3")
    parser.add_argument("steps", type=int, default=15)
    parser.add_argument("delay", type=float, default=.3)
    args = parser.parse_args(sys.argv[1:])

    print("Total: 100")

    for i in range(args.steps):
        print("Current: {}".format(i + 1, args.steps))
        sys.stdout.flush()
        time.sleep(args.delay)


if __name__ == '__main__':
    main()