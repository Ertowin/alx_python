import random
number = random.randint(-10,10)

for number in range(-10,10):
   if number > 0:
     print(number, " is positive ")
     if number == 0:
        print(number, "is Zero")
        if number < 0:
           print( number,"is negative")
