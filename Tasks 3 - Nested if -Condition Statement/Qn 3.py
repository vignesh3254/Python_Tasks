sub1=int(input("Enter Your Score1:"))
sub2=int(input("Enter Your Score2:"))
sub3=int(input("Enter Your Score3:"))

avg_score = (sub1+sub2+sub3)/3
print(avg_score)

if avg_score>=50:
    if sub1>=40 and sub2>=40 and sub3>=40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")
