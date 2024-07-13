#3)Try changing one of the elements in the tuple and observe what happens.
"""
colors=("Red","Black","White","Pink")
colors[0]="Sandal"
print(colors)#output:TypeError: 'tuple' object does not support item assignment.
"""

#You can change convert tuple to list

colors=("Red","Black","White","Pink")
c=list(colors)
c[0]="Sandal"
print(tuple(c))
