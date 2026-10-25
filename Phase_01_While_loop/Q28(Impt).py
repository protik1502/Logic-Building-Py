# Find the smallest digit in the given number.

user_input = int(input("Enter your number: "))
def smallest (num):
    copy_num = num
    num = abs(num)
    small = 9
    if num > 0:
        while num > 0 :
            digit = num % 10
            if digit < small:
                small = digit
            num = num // 10
        print(f"Smallest digit in {copy_num} is {small}.")
    else:
        print("Don't enter zero as input")
smallest(user_input)