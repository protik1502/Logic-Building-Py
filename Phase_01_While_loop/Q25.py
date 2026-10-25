# Find and print the sum of all factors of the given number. 

user_input = int(input("Enter your number: "))
factors = 1
sum = 0
if user_input > 0:
    while user_input >= factors:
        if user_input % factors == 0:
            sum = sum + factors
        factors += 1
    print(f"Sum of all the factors of {user_input} is {sum}")
else:
    print("Enter number greater than zero.")