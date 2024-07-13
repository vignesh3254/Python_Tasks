#4)Remove the person's city from the dictionary and print the updated dictionary.

info = {
    "name":"Anbu",
    "age":26,
    "city":"Erode"
    }
print(info)
info.pop("city")
print(info)

#usig del remove item

del info["age"]
print(info)
