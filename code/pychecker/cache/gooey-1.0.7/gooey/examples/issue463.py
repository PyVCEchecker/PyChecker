from gooey import Gooey, GooeyParser

def main():
   parser = GooeyParser(
       description="A GooeyParser example",
      # formatter_class=argparse.ArgumentDefaultsHelpFormatter,
   )
   required_group = parser.add_argument_group(
       "Required arguments",
       "These options are mandatory "
   )

   required_group.add_argument("-a", "--a_argument", required=True, help="This is a argument.")

   required_group.add_argument(
       "-b",
       "--b_argument",
       type=int,
       required=True,
       default=5,
       help="This is a long text. This is a long text. This is a long text. This is a long text. ",
   )
   parser.parse_args()

def _main_():

   Gooey(main,
         program_name="Reproduce something",
         tabbed_groups=True)()

if __name__ == "__main__":
   _main_()