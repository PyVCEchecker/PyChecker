import time
def measure(x):
    time.sleep(1)
    print(x+" has been measured")
    time.sleep(1)
def mixIngredients():
    time.sleep(1)
    print("Batter is mixed")
    time.sleep(1)
def pourBatter():
    time.sleep(1)
    print("Batter is poured")
    time.sleep(1)
def setOvenTempTo(i):
    print("Setting oven temp")
    time.sleep(0.2)
    print("Heating up...")
    print("Ready in:")
    for y in range(0,int(i/100)):
        print(str(int(i/100)-y)+" hours")
        time.sleep(1)
    print("Oven temperature is set to " + str(i) + " degrees")
    time.sleep(1)
def bakeBatter():
    print("Baking first layer....")
    time.sleep(1)
    print("First layer baked")
    time.sleep(1)
    print("Baking second layer....")
    time.sleep(1)
    print("Second layer baked")
    time.sleep(1)
    print("Baking third layer....")
    time.sleep(1)
    print("Third layer baked")
    time.sleep(1)
    print("All layers are baked!")
    time.sleep(1)
def assembleCake():
    print("Assembling cake...")
    time.sleep(1)
    print("Cake is assembled and ready to be iced!")
    time.sleep(1)
def iceCake():
    print("Icing cake...")
    time.sleep(1)
    print("Cake is iced!")
    time.sleep(1)
    print("Congratulations! You baked a cake!")
def complete(*args):
    for i in args:
        measure(i)
    mixIngredients()
    pourBatter()
    setOvenTempTo(500)
    bakeBatter()
    assembleCake()
    iceCake()