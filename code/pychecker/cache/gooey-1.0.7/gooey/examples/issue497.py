import argparse



from gooey import GooeyParser, Gooey

@Gooey(program_description="DUCK MY FAT COCK")
def main():
    parser = argparse.ArgumentParser(description="Hello world!")
    parser.add_argument(
        nargs="*",
        default=["foo bar"],
        dest="multi_arg",
    )
    import time
    args = parser.parse_args()
    for i in range(1000):
        # import time
        # # time.sleep(1)
        # print("HI")
        print(time.time())
    print(args)


if __name__ == "__main__":
    main()