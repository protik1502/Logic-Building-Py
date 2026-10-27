# Print all even numbers between 1 and user input.

user_input = int(input("Enter your number: "))
if user_input > 0:
    for i in range(1,user_input):
        if i % 2 == 0:
            print(i,end=" ")
else:
    print("Enter the number greater than 0.")