import re
import itertools

r = r'\b((?:file|https?)://[^\s<>]*)'
t = 'hello world https://www.url-with-querystring.com/?url=has-querystring asdf asd sih \n\nhttp://www.example.com'


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

# print(list(grouper(re.finditer(r, t[:-26]), 2)))

# identity = lambda x: x

def iddd(*args):
    print("Uhh??")
    print(args)

# print(re.split(r, 'http://www.example.com'))
# print(re.split(r, 'Hello world!\n\nhttps://www.example.com'))
# print(re.split(r, 'file://www.example.com'))
# print(re.split(r, 'some text file://www.example.com some more text http://www.example.com http://www.example.com'))


def ddothing(x):
    textStream = iter(re.split(r, x))
    for item in textStream:
        plaintext = item
        url = next(textStream, None)
        print(repr(plaintext))
        if url:
            print(repr(url))
    # try:
    #     while textStream:
    #         plaintext = next(textStream)
    #         url = next(textStream, None)
    #
    #         print(repr(plaintext))
    #         if url:
    #             print(repr(url))
    # except StopIteration:
    #     pass

ddothing('http://ww.example.com\n\nhttps://asdfasdf.com')
print('==========================')
ddothing('http://ww.example.com')
print('==========================')
ddothing('HelloWorld http://ww.example.com\n\nhttps://asdfasdf.com')
print('==========================')
ddothing('')

#
#
# for plaintext, url in grouper(re.split(r, ''), 2):
#     self.WriteText(plaintext)
#     if url:
#         self.BeginTextColour(self.url_colour)
#         self.BeginUnderline()
#         self.BeginURL(url)
#         self.WriteText(url)
#         self.EndURL()
#         self.EndUnderline()
#         self.EndTextColour()


