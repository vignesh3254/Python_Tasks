#Qn.Write a program that classifies the temperature into various categories such as "Freezing", "Cold", "Warm", and "Hot" based on the following conditions:
"""
1)If the temperature is below 0°C, it is "Freezing".If the temperature is between 0°C and 10°C, it is "Cold".
2)If the temperature is between 10°C and 25°C, it is "Warm".
3)If the temperature is above 25°C, it is "Hot".
"""

temp=int(input("Enter a Temperature:"))
if temp>0:
    if temp<25:
        if temp>0 and temp<=10:
            print("Cold")
        else:
            print("Warm")
    else:
        print("Hot")
else:
    print("Freezing")
