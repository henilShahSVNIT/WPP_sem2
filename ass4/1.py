t=int(input())

for i in range (t):
    str=(input())
    p2 = len(str)
    p = len(str)
    p /= 2
    s=list(str)
    p = int(p)
    for i in range(p):
        char1 = s[i]
        char2 = s[-i-1]
        if(char1 > char2): #swapping whoever is bigger
            s[i] = char2
        else:
            s[-i-1] = char1

    count = 0
    for i in range(p2):
        if(s[i] != str[i]):
            count+=abs(ord(str[i])-ord(s[i])) #abs is absolute value (gives positive) and ord is ascii

    print(count,"\n")