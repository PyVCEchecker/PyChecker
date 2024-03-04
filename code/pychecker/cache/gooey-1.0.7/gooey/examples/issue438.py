import os
import sys
import re

from gooey import Gooey, GooeyParser


@Gooey(advanced=True,  # toggle whether to show advanced config or not
       show_config=True,  # skip config screens all together
       program_name='Вне рамок',  # Defaults to script name
       program_description="Мимо пролетел единорог",
       # Defaults to ArgParse Description
       default_size=(610, 530),  # starting size of the GUI
       required_cols=1,  # number of columns in the "Required" section
       optional_cols=1,  # number of columbs in the "Optional" section
       dump_build_config=False,  # Dump the JSON Gooey uses to configure itself
       load_build_config=None,  # Loads a JSON Gooey-generated configuration
       language = 'russian'
       )
def main():
    parser = GooeyParser(description="""Хотите ли вы купить хотдог?""")
    sg = parser.add_argument_group(
        "", gooey_options={'columns': 1})
    sg.add_argument('--Checkbox',
                    action='store_true',
                    widget="CheckBox",
                    help="Очень важный параметр")

    args = parser.parse_args()

    print("Русский текст, который не кодируется")


if __name__ == "__main__":
    main()