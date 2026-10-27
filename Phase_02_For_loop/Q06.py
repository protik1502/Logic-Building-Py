# Calculate and print the factorial of a given number.

user_input = int(input("Enter your number : "))
def factorials(num):
    start = 1
    if num == 0:
        return f"The factorial of {num} is {start}"
    elif num > 0 :
        for i in range (start,num + 1):
            start *= i
        return f"The factorial of {num} is {start}"
print(factorials(user_input))