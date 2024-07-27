#3.

"""Use each of map, filter, and reduce to fix the broken code.

from functools import reduce
"""

"""
a)Use map to print the square of each numbers rounded to three decimal places.
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
"""
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

def k(a):
    return round(a**2,3)

m=map(k,my_floats)
print(list(m))

"""
b)Use filter to print only the names that are less than
or equal to seven letters
my_names = ["Python", "Programming", "Language", "Technology", "Cloud"]
"""

my_names = ["Python", "Programming", "Language", "Technology", "Cloud"]
def a(b):
    a=len(b)
    if a<=7:
        return a
        
        
f=filter(a,my_names)
print(list(f))

"""
c)Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
"""

my_numbers = [4, 6, 9, 23, 5]

from functools import reduce


def n(a,b):
    return a*b
b=reduce(n,my_numbers)
print(b)

"""
d)Fix all three respectively.
map_result = list(map(lambda x: x, my_floats))
filter_result = list(filter(lambda name: name, my_names, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)

print(map_result)
print(filter_result)
print(reduce_result)
"""


map_result = list(map(lambda x: round(x**2,3), my_floats))
filter_result = list(filter(lambda name: len(name)<=7, my_names))

from functools import reduce
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)











