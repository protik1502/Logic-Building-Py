# Check whether the given number is a palindrome.

user_input = int(input("Enter your number:"))
original_num = user_input
reversed_num = 0
while True:
    reminder = user_input % 10
    reversed_num = (reversed_num * 10) + reminder
    user_input = user_input // 10
    if user_input == 0:
        break
if original_num == reversed_num:
    print(f"The number is palindrome.")
else:
    print("The number is not palindrome.")

