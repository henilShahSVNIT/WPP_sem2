t=int(input())

for i in range (t):
    N=int(input())
    temp = N
    which = 0
    height = 1
    for j in range (N):
        if(which % 2 == 0):
            height*=2
        else:
            height+=1
        which+=1
    print(height,"\n")
    