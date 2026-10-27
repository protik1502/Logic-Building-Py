# Find and print the sum of all factors of the given number.

user_input = int(input("Enter your number: "))
user_input = abs(user_input)
sum = 0
if user_input == 0:
    print(f"The sum of all the factors are : {sum}")
else:
    for i in range (1,user_input + 1):
        if user_input % i == 0:
            sum += i
    print(f"The sum of all factors are : {sum}")