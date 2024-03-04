# Learning tool for teaching the Cake Baking Analogy 

Meant to make the analogy literal so that beginners can better understand the basics of functions.

## 1.1 Functions:
(All functions sleep one second after they run except complete)\
measure: waits one second then prints its string argument\
mixIngredients: sleeps for one second then prints "Batter is mixed"\
pourBatter: waits one second then prints "Batter has been poured"\
setOvenTempTo: prints "Setting oven temp", waits 0.2 seconds, prints "Heating up...", prints "Ready in x hours" where x is the oven temperature divided by 100 then stops and prints "Oven temperature set to y degrees" where y is its int argument\
bakeBatter: prints "Baking x layer" and then "x layer baked" where x is the ordinal form of 1 through 3 and then prints "All layers are baked!"\
assembleCake: prints "Assembling cake..." then sleeps for 1 second then prints "Cake is assembled and ready to be iced!"\
iceCake: prints "Icing cake..." then "Cake is iced!"\
complete: executes every function and takes unlimited string arguments which are use in measure and uses 500 for setOvenTemp argument.