import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
if number < 0:
      last_digit = - last_digit

      if number > 5:
              print("Last digit of ", number, "is", last_digit, "and is greater than 5")
      if number == 0:
              print("Last digit of ", number, "is", last_digit, "and is 0")
      if number < 6:
            print("Last digit of ", number, "is", last_digit, "is less than 6 and not zero")
            

