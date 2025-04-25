t1 = int(input())
t2 = int(input())

#xor(a,b) = a ^ b

xor_max = 0
for i in range(t1,t2):
    for j in range(i+1,t2):
        xor = i ^ j
        if(xor > xor_max):
            xor_max = xor

print(xor_max)