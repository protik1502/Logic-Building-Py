# Find and print the product of all the digits of a given number.

user_input = int(input("Enter your number: "))
def sum_of_digits (num):
    sum = 1
    num = abs(num)
    if num == 0:
        sum = 0
    else:
        while num > 0:
            sum *= num % 10
            num = num // 10
    print("Product of all the digits:",sum)
sum_of_digits(user_input)
