# Calculate and print the sum of all odd numbers from 1 to n.

user_input = int(input("Enter your number: "))
def sum_odd (num):
    count = 1
    total_sum = 0
    if num > 0:
        while num >= count:
            total_sum = total_sum + count
            count += 2
        print("Sum of all the odd numbers:",total_sum)
    else:
        print("Enter a valid number.")
sum_odd(user_input)