from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description="Gooey example")
    parser.add_argument("-a", "--myargument", action="store_true")
    args = parser.parse_args()
    print(args)
    print(args.myargument)
    print(type(args.myargument))


if __name__=="__main__":
    main()