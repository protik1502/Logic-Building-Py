# Calculate and print the factorial of a given number.

user_input = int(input("Enter your number: "))
def factorial (num):
    sum = 1
    count = 1
    if num >= 0:
        while num >= count:
            sum*=count
            count += 1
        print(f"Factorial of {num} : {sum}")
    else:
        print("Enter a valid number")
factorial(user_input)