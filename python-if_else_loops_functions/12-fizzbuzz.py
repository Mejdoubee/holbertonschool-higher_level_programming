#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(end="FizzBuzz ")
        elif (i % 3 == 0):
            print(end="Fizz ")
        elif (i % 5 == 0):
            print(end="Buzz ")
        else:
            print(f"{i}", end=" ")
