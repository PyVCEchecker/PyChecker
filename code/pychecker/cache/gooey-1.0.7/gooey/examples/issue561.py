from gooey import Gooey, GooeyParser

import matplotlib.pyplot as plt # hangs when imported here

@Gooey
def main():
    argparser = GooeyParser()
    argparser.add_argument('foo')

    args = argparser.parse_args()

    # import matplotlib.pyplot as plt # works as expected when imported here

    print(args.foo)


if __name__ == '__main__':
    main()