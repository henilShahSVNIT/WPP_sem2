t=(input())
l = len(t)

#Pangrams are sentences constructed by using every letter of the alphabet at least once
zeroes = [x-x for x in range (26)]

t = list(t)
for i in range (l):
    temp = ord(t[i]) - 97
    if(temp>=0):
        zeroes[temp]+=1

for i in range (26):
    if(zeroes[i]==0): #if any letter has zero occurence its not a panagram
        print("not pangram")
        break
    if(i==25): #if all letters checked >0 then its a panagram
        print("panagram")
