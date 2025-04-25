class employee :
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __add__(self,other):
        return self.salary+other.salary
    def __sub__(self,other):
        return self.salary-other.salary
name=input("Enter name of employee number 1 : " )
s=float(input("Enter salary of employee number 1 : "))
e1=employee(name,s)
name=input("Enter name of employee number 2 : " )
s=float(input("Enter salary of employee number 2 : "))
e2=employee(name,s)
print("Combined salary : ",e1+e2)
if(e1-e2>0):
    print(e1.name,"has greater salary")
elif(e1-e2<0):
    print(e2.name,"has greater salary")
else:
    print("Both have same salary")