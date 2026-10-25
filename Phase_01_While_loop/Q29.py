# Find the largest digit in the given number.

user_input = int(input("Enter your number: "))
def largest_number (num):
    copy_num = num
    num = abs(num)
    large = 0
    if num > 0 :
        while num > 0 :
            digit = num % 10
            if digit > large:
                large = digit
            num = num // 10
        print(f"The largest digit in {copy_num} is {large}.")
    else:
        print("Don't enter input as a zero.")
largest_number(user_input)