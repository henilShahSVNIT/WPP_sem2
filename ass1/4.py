sample=[x for x in range(1,10001,1)] #list from 1 to 10000
classes={0:[],1:[],2:[],3:[],4:[]} #empty dictionaries with keys as remainders 
for x in sample:
    rem=x%5
    classes[rem].append(x)
u=set()
for i in range (0,5):
    u=u.union(set(classes[i])) #union of all 5 sets
if list(u)==sample:
    print("Verified")
else:
    print("Not verified")