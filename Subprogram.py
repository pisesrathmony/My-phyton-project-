#subprogram(procedure)
def Foods():
    print("Pizza")
    print("Rice")
    print("pasta")
    print("Sushi")
Foods()

#subprogram(Function)
def plus (x,y):
    return ( x + y) 
print(plus(5 ,5))

import random
def randomfood():
    list = ["Pizza", "pasta", "sushi"]
    print(random.choice(list))

randomfood()

