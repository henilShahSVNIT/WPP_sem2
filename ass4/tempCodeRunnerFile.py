t=(input())
l = len(t)

zeroes = [x-x for x in range (26)]

t = list(t)
for i in range (l):
    temp = ord(t[i]) - 97
    if(temp>=0):
        zeroes[temp]+=1

for i in range (26):
    if(zeroes[i]==0):
        print("not pangram")
        break
    if(i==25):
        print("panagram")