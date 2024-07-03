b=input('enter your name')
v='aeiou'
count=0
for i in b:
    for j in v:
        if i==j:
           print(j)
           count=count+1
print(count)
        
        
