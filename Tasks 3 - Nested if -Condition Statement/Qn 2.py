#Qn 2.Write a program that calculates the final grade of a student based on their score and whether they completed extra credit assignments. Use the following conditions:
"""
1)If the score is above 90 and extra credit is completed,the final grade is "A+".
2)If the score is above 90 and extra credit is not completed, the final grade is "A".
3)If the score is between 80 and 90 and extra credit is completed, the final grade is "B+".
4)If the score is between 80 and 90 and extra credit is not completed, the final grade is "B".
*)Repeat similar logic for grades "C", "D", and "F".
"""


score=int(input("Enter Your Score:"))
extra=input("Assignment Done:Yes/No:")
if score>=90:
    if extra=="Yes":
        print("A+")
    else:
        print("A")
else:
    if score>=80:
        if extra=="Yes":
            print("B+")
        else:
            print("B")
    else:
        if score>=70:
            if extra=="Yes":
                print("C+")
            else:
                print("C")
        else:
            if score>=60:
                if extra=="Yes":
                    print("D+")
                else:
                    print("D")
            else:
                print("Fail")
