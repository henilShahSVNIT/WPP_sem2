import random

list = [random.choice([0, 1]) for i in range(100)]
max_run = 0
cur_run = 0
for num in list:
    if num == 0:
        cur_run += 1
        max_run = max(max_run, cur_run)
    else:
        cur_run = 0
print("the list is : ",list,"\nthe maximum run of zeroes is : ", max_run)