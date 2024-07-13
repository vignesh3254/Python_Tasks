#3)Update the person's age and print the updated dictionary.
info = {
    "name":"Anbu",
    "age":26,
    "city":"Erode"
    }
info["age"]=28
print(info)

#using update() method

info.update({"age":30})
print(info)
