#!/usr/bin/python3
"""Module that prints numbers 1 to 100 with FizzBuzz rules."""


def fizzbuzz():
    """Print numbers 1 to 100, replacing multiples of 3, 5, or both."""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
