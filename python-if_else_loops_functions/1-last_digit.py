#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10
if(number < 0):
    last_num = -last_num

print(f"The last digit of {number} is ",end="")
if((last_num < 5) & (last_num != 0)):
    print(f"{last_num} and is less than 6 and not 0")
elif(last_num > 5):
    print(f"{last_num} and is greater than 5")
else:
    print(f"{last_num} and is 0")
