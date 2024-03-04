from gooey import Gooey, GooeyParser

@Gooey(dump_build_config=True)
def main():
    parser = GooeyParser(description="Gooey example")
    parser.add_argument("-a", "--myargument", choices=['a','b'], default='a')
    args = parser.parse_args()
    print(args)
    print(args.myargument)
    print(type(args.myargument))


if __name__=="__main__":
    main()