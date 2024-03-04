

# surprising Python behavior

def foo():

    funcs = []

    for i in range(10):
        funcs.append(lambda x: print('x', i))

    for func in funcs:
        func("yo")

foo()

def thingieMcThingFace():
    def f(x)




