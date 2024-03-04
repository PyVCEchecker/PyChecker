import argparse
from gooey import Gooey

@Gooey(dump_build_config=True, advanced=False)
def main():
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+',
                     help='an integer for the accumulator')

  args = parser.parse_args()
  print 'Good job!'

if __name__ == '__main__':
  main()
