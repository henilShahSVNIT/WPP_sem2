n=int(input("Enter the number : "))

def sum_digits(k): #adds the digits of the current number
    sum = 0
    while(k > 9):
        temp = k % 10
        k -= temp
        k /= 10
        sum += temp
    temp = k % 10
    k -= temp
    k /= 10
    sum += temp
    return sum

while(n>9): #keeps calling function till number is one digit
    n = sum_digits(n)

print(n)