"""
define a class Negativenumber
write a program that prompts the user to enter a positive number

raise the custom exception if the  user enter a negative number

use a try-except block to catch custom exception and print an appropriate message
"""

class NegativeNumber(Exception):
    pass

try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise NegativeNumber
    print(f"You entered: {number}")
except NegativeNumber as e:
    print(f"Error!!!{e}")
