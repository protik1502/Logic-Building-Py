# Calculate and print the factorial of the given number.

user_input = int(input("Enter your: "))
def factorial (n):
    total_sum = 1
    count = 1
    while True:
        total_sum *= count
        count += 1
        if n < count:
            break
    print(f"The factorial of {n} is {total_sum}")
factorial(user_input)
        
