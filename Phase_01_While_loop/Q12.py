# Reverse the given number and print the reversed value.

user_input = int(input("Enter the number to be reversed: "))
def reverse_number(num):
    num = abs(num)
    rev = ""
    if num == 0:
        return num
    else:
        while num > 0 :
            rev = rev + str(num % 10)
            num = num // 10
        return int(rev)
print("Reversed order of the number is:",reverse_number(user_input))
