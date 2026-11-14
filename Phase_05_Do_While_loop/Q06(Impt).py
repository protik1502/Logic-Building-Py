# Reverse the given number and print the reversed value.

user_input = int(input("Enter your number: "))
reversed_num = 0
while True:
    remainder = user_input % 10
    reversed_num = (reversed_num * 10) + remainder
    user_input = user_input // 10
    if user_input == 0:
        break
print(f"The reversed number is {int(reversed_num)}")
