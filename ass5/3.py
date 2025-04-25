#to find next lexicographically greater word

def findNext(s):
    s = list(s)
    length = len(s)
    
    i = length - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    
    if i == -1:
        return "no answer"
    
    j = length - 1
    while s[j] <= s[i]:
        j -= 1

    s[i], s[j] = s[j], s[i] #swap

    left = i + 1
    right = length - 1

    while left < right: #sort the remaining string 
        s[left],s[right] = s[right],s[left]
        left +=1
        right -=1
    return "".join(s)

t = int(input())
for _ in range(t):
    word = input().strip() #to remove any excess white spaces
    print(findNext(word))

#logic : we go through the string right to lef to find the first char1<char2 then we swap it with the first
#letter and sort the remaining string anti alphabetically