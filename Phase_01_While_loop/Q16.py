#  Check whether the given number is a Perfect number.
user_input = int(input("Enter your number: "))
def perfect_number (num):
    if num == 0:
        return "The number is not perfect."
    count = 1
    sum_of_factors = 0
    while num > count :
        if num % count == 0:
            sum_of_factors = sum_of_factors + count
        count += 1
    if num == sum_of_factors:
        return "The number is perfect."
    else:
        return "The number is not perfect."
print(perfect_number(user_input))

'''
A perfect number is a positive integer that is equal to the sum of its proper divisors.

Key Examples:

• 6: Its proper divisors are (1, 2,) and (3). Adding them up gives (1 + 2 + 3 = 6).
• 28: Its proper divisors are (1, 2, 4, 7,) and (14). Adding them up gives (1 + 2 + 4 + 7 + 14 = 28).

'''