t=int(input()) #number of test cases
list=[]
c=0
while c<t:
    list.append(int(input()))  
    c+=1
for x in list:
    c=0
    temp=x
    while temp>0:
        d=temp%10
        if(x%d==0):
            c+=1
        temp=temp//10 #// : floor division : rounds the division to neartest whole number
    print(c)