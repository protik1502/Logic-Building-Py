# Count and print the total number of digits of a given number. 

user_input = int(input("Enter your number: "))
def num_of_digits (num):
    num = abs(num)
    count = 0
    if num == 0:
        return 0
    else:
        while num > 0:
            num = num // 10
            count += 1
        return count
print("Total number of digits are:",num_of_digits(user_input))