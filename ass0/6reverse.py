num = input('enter number : ')

len = len(num)
sum = 0
zero = 1
for i in range(len):
    zero = zero * 10

num = int(num)

for i in range(len):
    j = num % 10
    sum = sum + (j*zero)
    zero = zero / 10
    num = num - j
    num = num / 10
sum = sum / 10

print('the reversed num is {0}'.format(sum))
