#5)Loop through the dictionary and print each key and value

info = {
    "name":"Anbu",
    "age":26,
    "city":"Erode"
    }

for i in info:
    print("1.Keys :",i) # Keys
    print("1.Values :",info[i]) # Values
    
print(end="\n")

#another method
for i in info.keys():
    print("2.Keys:",i) 
for i in info.values():
    print("2.Values:",i)
    
print(end="\n")

#another method
for x,y in info.items():
    print("3.Keys and Values",x,y)
