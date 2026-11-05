# Print the multiplication tables for all numbers from 1 to n.

user_input = int(input("Enter your number: "))
for i in range(1,user_input + 1):
    print(f"Multiplication of table of {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
