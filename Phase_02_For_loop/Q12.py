# Print all factors of the given number.

user_input = int(input("Enter your number: "))
user_input = abs(user_input)
print(f"The factors of {user_input} are : ")
if user_input == 0:
    print(user_input)
else:
    for i in range (1,user_input + 1):
        if user_input % i == 0:
            print(i,end=" ")