import sys
points=[] #list of all points
n=int(input("Enter number of points(10 given in question) : "))
closest={} #dictionary to store closest for all points
for i in range(0,n,1):
    print("point number : ",i+1)
    x=float(input("Enter x co-ordinate "))
    y=float(input("Enter y co-ordinate "))
    z=float(input("Enter z co-ordinate "))
    point=(x,y,z)
    points.append(point)
    closest.update({point:[]}) 
for p1 in points:
    d=sys.maxsize  #max int size
    for p2 in points:
        if(p1!=p2):
            x1=(p1[0]-p2[0])**2    
            y1=(p1[1]-p2[1])**2
            z1=(p1[2]-p2[2])**2
            dist=x1+y1+z1     #distance formula
            if(dist<=d):
                if(dist==d):
                    closest[p1].append(p2)
                else:
                    d=dist
                    closest[p1]=[p2]
for p in points:
    print(p,"\t",closest[p])