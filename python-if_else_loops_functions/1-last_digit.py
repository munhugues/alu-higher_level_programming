#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(repr(number)[-1])
if(number > 0):
    if((last_num < 5) & (last_num != 0)):
        print(f"The last digit of {number} is {last_num} and is less than 6 and not 0")
    elif(last_num > 5):
        print(f"The last digit of {number} is {last_num} and is greater than 5")
elif(number < 0):
    if((last_num < 5) & (last_num != 0)):
        print(f"The last digit of {number} is -{last_num} and is less than 6 and not 0")
    elif(last_num > 5):
        print(f"The last digit of {number} is -{last_num} and is greater than 5")
else:
    print(f"The last digit of {number} and is {last_num}")

