import sys
from enum import Enum
from gooey import Gooey, GooeyParser

class TestMode(Enum):
    PRODUCTION = 0
    VALIDATION = 1
    TEST = 2
    NONE = 3

@Gooey()
def main() -> int:
    parser = GooeyParser(description="Show unexpected behaviour")

    parser.set_defaults(mode=TestMode.PRODUCTION)
    mode = parser.add_mutually_exclusive_group()

    mode.add_argument(
        "--none",
        metavar="None",
        action="store_const",
        const=TestMode.NONE,
        help="Don't use any special validation logic",
    )

    mode.add_argument(
        "--validation",
        metavar="Validation",
        action="store_const",
        const=TestMode.VALIDATION,
        help="Target the validation database.",
    )
    mode.add_argument(
        "--test",
        metavar="Test",
        dest="mode",
        action="store_const",
        const=TestMode.TEST,
        help="Target the test database.",
    )

    print(parser.parse_args())

main()