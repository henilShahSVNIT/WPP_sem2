import string
s=input("Enter word ")
s2="" #output string
c=1
for x in s:
    if c%2==0: #other way could be (x,strlen,2)
        x=str(x)
        s2+=x.upper() 
        
    else:
        s2+=x
    c+=1
print(s2)