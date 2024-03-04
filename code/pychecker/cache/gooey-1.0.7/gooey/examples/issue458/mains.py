import argparse
from gooey import Gooey
from examples.issue458.resource import ConstantArray

def get_resource(num):
    return ConstantArray[num]

@Gooey
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ResourceNumber")
    args = parser.parse_args()

    print(get_resource(int(args.ResourceNumber)))

if __name__ == "__main__":
    main()