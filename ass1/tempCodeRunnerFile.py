names=[]
n=int(input("Enter number of students : "))
for i in range(n):
    print("Student ",i+1)
    s=input("Enter name : ")
    names.append(s)
print("Names upto 15 characters")
for x in names:
    print(x[:15])
print("Reversed names")
for x in names:
    length=0-len(x)-1
    print(x[-1:length:-1])