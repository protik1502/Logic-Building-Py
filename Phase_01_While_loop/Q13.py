# Check whether the given number is a palindrome or not.

user_input  = int(input("Enter your desired number: "))
def palindrome (num):
    num = abs(num)
    original_num = num
    reverse = ""
    if num == 0:
        return "The number is Palindrome"
    else:
        while num > 0:
            reverse = reverse + str(num % 10)
            num = num // 10
        reverse = int(reverse)
        if reverse == original_num:
            return "The number is Palindrome"
        else:
            return "The number is not Palindrome"
print(palindrome(user_input))
            