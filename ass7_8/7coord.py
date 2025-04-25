import math

class XYspace:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mag = math.sqrt(x**2 + y**2)
        self.rotation = math.atan(y / x)

    def dist(self,other):
        return(math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2))
    
    def dot(self,other):
       dotx =  self.x*other.x
       doty =  self.y*other.y
       return(dotx + doty)
    
    def cross(self,other):
        crossk1 = self.x*other.y
        crossk2 = self.y*other.x
        crk = crossk1 - crossk2
        return(str(crk)+" k")

class XYZspace(XYspace):
    def __init__(self,x,y,z):
        self.z = z
        self.x = x
        self.y = y
        self.mag = math.sqrt(x**2 + y**2 + z**2)
        self.rotation = math.atan(math.sqrt(y**2 + z**2) / x)

    def dist(self,other):
        return(math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.y-other.y)**2))
    
    def dot(self,other):
       dotx =  self.x*other.x
       doty =  self.y*other.y
       dotz = self.z*other.z
       return(dotx + doty + dotz)
    
    def cross(self,other):
        crossk1 = self.x*other.y
        crossk2 = self.y*other.x
        crossi1 = self.y*other.z
        crossi2 = self.z*other.y
        crossj1 = self.x*other.z
        crossj2 = self.z*other.x
        crk = crossk1 - crossk2
        cri = crossi1 - crossi2
        crj = crossj1 - crossj2
        return(str(cri)+" i + "+str(crj)+" j + "+str(crk)+" k")

pick1 = int(input("Choose 2D space or 3D (Input 2 for 2D and 3 for 3D : "))
if(pick1 == 2):
    x1 = int(input("Enter x-coord of 1st point : "))
    y1 = int(input("Enter y-coord of 1nd point : "))
    x2 = int(input("Enter x-coord of 2st point : "))
    y2 = int(input("Enter y-coord of 2nd point : "))

    ele1 = XYspace(x1,y1)
    ele2 = XYspace(x2,y2)

    print("Distance = ",ele1.dist(ele2))
    print("Dot Product = ",ele1.dot(ele2))
    print("Cross Product ele1 x ele2 = ",ele1.cross(ele2))

else:
    x1 = int(input("Enter x-coord of 1st point : "))
    y1 = int(input("Enter y-coord of 1nd point : "))
    z1 = int(input("Enter z-coord of 1st point : "))
    x2 = int(input("Enter x-coord of 2st point : "))
    y2 = int(input("Enter y-coord of 2nd point : "))
    z2 = int(input("Enter z-coord of 2st point : "))

    ele1 = XYZspace(x1,y1,z1)
    ele2 = XYZspace(x2,y2,z2)

    print("Distance = ",ele1.dist(ele2))
    print("Dot Product = ",ele1.dot(ele2))
    print("Cross Product point1 x point2 = ",ele1.cross(ele2))

