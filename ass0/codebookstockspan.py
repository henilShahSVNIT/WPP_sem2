num = int(input())

max = 0
for i in range(num):
    a=int(input())

sequence = 0  
for i in range(num):
    if a[i] > a[i-1]:
        sequence = sequence + 1
    else:
        sequence = 1
    print(sequence," ")