list_a = [x for x in range (50)]
print("list a : ",list_a)

list_b = [i**2 for i in range (1,51)]
print("list b : ",list_b)

list_c=[]
count = 1
for i in range (97,123):
    str = ""
    for j in range (0,count):
        str+=chr(i)
    count+=1
    list_c.append(str)
print("list c : ",list_c)