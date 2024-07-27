#1.
"""
write a program that prompts the user to enter two numbers

perform division of the first number by second number

use a try - except block to handle any division by zero errors and
print an appropriate message
"""

a=int(input("Number 1:"))
b=int(input("Number 2:"))
try:
    if a//b:
        print("Two Numbers Divided Complete")
except:
    print("Error")

