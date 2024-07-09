#least number in a list without use method 
random=[2,6,4,9,3,5,36]
mini=random[0]
for i in random:
    if i < mini:
        mini=i
print(mini)

#largest number in a list without use method

for i in random:
    if i > mini:
        mini=i
print(mini)
