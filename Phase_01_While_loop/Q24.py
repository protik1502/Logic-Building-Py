# Print all factors of the given number.

user_input = int(input("Enter your number: "))
factors = 1
if user_input > 0:
    print(f"Factors of {user_input} : ")
    while user_input >= factors:
        if user_input % factors == 0:
            print (factors,end=" ")
        factors += 1
else:
    print("Enter number greater than zero.")