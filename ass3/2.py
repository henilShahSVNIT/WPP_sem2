def fibo(n): #returns nth fibo number
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

t=int(input())

for i in range (t):
    N=int(input())
    fiboNUM = 0
    temp = 0
    while(1):
        fiboNUM = fibo(temp)
        if(fiboNUM > N): #exceeds the number then notfibo
            print("IsNotFibo\n")
            break
        elif(N == fiboNUM):
            print("IsFibo\n")
            break
        temp+=1
