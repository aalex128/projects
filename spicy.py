#makes random number
#has user guess random number
import random
import time
import json




z = int(input("select your dificulty. 1 2 3:  "))
if z == 3:
    a = 200
    print("200 numbers")
if z == 2:
    a = 100
    print("100 numbers")
if z == 1:
    a = 10
    print("10 numbers")

y = int(input("choose your lives:  "))
b = time.perf_counter()


x = random.randint(1,a)

while True:
    check = int(input("what am i thinking of???   "))
    if check == x:
        print("you got it!")
        c = time.perf_counter()
        print("it took you.......    ")
        print(c-b, "seconds")
        print("you got" , a-(c-b) , "points")

        break
    else:
        if check > x:
            print("lower")
        if check < x:
            print("higher")
        y = y - 1
        print(f"lives: {y}")
        if y == 0:
            print("you lost :(   ")
            print(f"the number was: {x}")
            break
        continue
