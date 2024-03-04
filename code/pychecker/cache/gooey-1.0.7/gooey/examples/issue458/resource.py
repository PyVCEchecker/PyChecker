import argparse
from gooey import Gooey

ConstantArray = [
        'foo',
        'bar',
        'baz',
        'gat'
]


def fooobar():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="sup fam")
    args = parser.parse_args()

    print(args)


if __name__ == "__main__":
    Gooey(fooobar)()
