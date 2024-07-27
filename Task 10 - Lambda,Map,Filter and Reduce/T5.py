#5.
"""
Write a Python program using the map function to identify
whether each number In  a list Is even or odd
"""

li=[2,6,8,1,3,7,13]

b=map(lambda a:a%2==0,li)
print(list(b))


"""
Write another program using the filter function to
extract and print only the even numbers from the list
"""
i=[2,6,8,1,3,7,13]

b=filter(lambda a:a%2==0,i)
print(list(b))
