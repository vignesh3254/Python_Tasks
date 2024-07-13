#2)Add a new key-value pair for the person's job and print the updated dictionary.
info = {
    "name":"Anbu",
    "age":26,
    "city":"Erode"
    }
info["Job"]="IT"
print(info)

#using update() method

info.update({"Native":"Kumarapalayam"})
print(info)
