def transform_list(lst):
    for i in range(len(lst)): 
        if lst[i] %3== 0: 
            lst[i] = lst[i] // 3 
        elif lst[i] % 2 == 0: 
            lst[i] = lst[i] * 2 
        else: 
            lst[i] = lst[i] + 1

numbers = [2, 3, 5, 6, 9] 
x = 2

for i in range(x):
    transform_list(numbers) 
    numbers = [num + numbers[i] for num in numbers] 
    x += 1 if numbers[i] % 2 == 0 else 0

print(numbers)