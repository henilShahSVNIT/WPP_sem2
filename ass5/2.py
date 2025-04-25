t = int(input())

#we check all possible additions for t and multiply the addants to find max
for i in range (t):
    max = 0
    k = int(input())
    for j in range (1,k):
        temp = j * (k-j)
        if(temp > max):
            max = temp
    print(max,"\n")