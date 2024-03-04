'''
A Gooey example showing use of richtext display in the console pannel.
'''
import os

from gooey import Gooey, GooeyParser

@Gooey()
def main():
    parser = GooeyParser(description='Just display the console')

    parser.add_argument('--host', help='Ze host!', default=os.environ.get('HOST'))
    args = parser.parse_args()

if __name__ == '__main__':
    main()