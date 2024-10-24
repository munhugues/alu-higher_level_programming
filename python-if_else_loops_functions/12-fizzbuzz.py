#!/usr/bin/python3
def fizzbuzz():
    n = 1
    while n <= 100:
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(n, end=" ")
        n += 1
