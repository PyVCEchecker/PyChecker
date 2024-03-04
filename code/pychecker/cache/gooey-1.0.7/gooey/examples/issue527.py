'''
A Gooey example showing use of richtext display in the console pannel.
'''

from gooey import Gooey, GooeyParser
from colored import stylize, attr, fg, bg
from colored import fore, back, style


@Gooey(richtext_controls=True, auto_start=True)
def main():
    parser = GooeyParser(description='Just display the console')

    args = parser.parse_args()
    # print(stylize("This is bold.", attr("bold")))
    # print(stylize("This is underlined.", attr("underlined")))
    # print(stylize("This is green.", fg("green")))
    # print(stylize("This is red.", fg("red")))
    # print(stylize("This is blue and bold.", fg("blue") + attr("bold")))
    # print('%s%s Hello World !!! %s' % (fg('white'), bg('yellow'), attr('reset')))
    # print('%s Hello World !!! %s' % (fg(1), attr(0)))
    # print (fore.LIGHT_BLUE + back.RED + style.BOLD + "Hello World !!!" + style.RESET)
    # for i in range(0, 256, 40):
    #     for j in [0,1,2,4,5,7,8,21,22,24,25,27,28]:
    #         print('%s Hello World !!! %s' % (fg(i), attr(j)))
    # for i in range(256):
    #     print(stylize('Hello World !!!', bg(i) + fg(i)))
    print(stylize('Hello world!', fg('#ff0001') + attr('bold')))
    print("{} Hey, hey!".format(attr('bold')))
    print('yo')
    print('yo')
    # for j in [0,1,2,4,5,7,8,21,22,24,25,27,28]:
    #     print(stylize(str(j) + ' - Hello World !!!' , fg('red') + bg('blue') + attr(j)))

if __name__ == '__main__':
    main()