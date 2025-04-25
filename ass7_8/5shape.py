class Shape:
    def __init__(self, *args):
        if len(args) == 1:
            self.peri = 3.14 * 2 * args[0]
            self.area = (3.14 * args[0] * args[0])
        elif len(args) == 2:
            self.peri = (2*(args[0] + args[1]))
            self.area = args[0] * args[1]
        print("Perimeter : ",self.peri,"\nArea : ",self.area)

class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius)

class Rectangle(Shape):
    def __init__(self,len,bre):
        super().__init__(len,bre)

n = int(input("Number of cases : "))
for i in range(n):
    pick = int(input("Enter 1 for circle and 2 for rectangle : "))
    if(pick == 1):
        r = int(input("Enter Radius : "))
        Circle(r)
    else:
        l = int(input("Enter Length : "))
        b = int(input("Enter Breadth : "))
        Rectangle(l,b)
    
