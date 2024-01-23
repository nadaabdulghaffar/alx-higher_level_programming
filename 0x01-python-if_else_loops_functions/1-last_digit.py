#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10 if number > 10 else number % -10
if lastDigit == 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
elif lastDigit < 6:
    print("Last digit of {:d} is {:d}".format(number, lastDigit), end=" ")
    print("and is less than 6 and not 0")
else:
    print("Last digit of {:d} is {:d}".format(number, lastDigit), end=" ")
    print("and is greater than 5")
