import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

for number in range(-10000, 10000):
        if number > 5:
              print("Last digit of {} is 5 {}".format(number, "and is greater than 5"))
        if number == 0:
              print("Last digit of {} is 0 {}".format(number, "and is 0"))
        if number < 6:
              print("Last digit of {} is 6 {}".format(number, "and is less than 6 and not 0"))
            

