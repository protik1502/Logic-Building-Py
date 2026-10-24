# Find and print the sum of digits of the given number

user_input = int(input("Enter your number: "))
def sum_of_all_numbers (num):
    num = abs(num)
    add = 0
    while num > 0:
        add = add + num % 10
        num = num // 10
    return add
print("Sum of all the digits:",sum_of_all_numbers(user_input))