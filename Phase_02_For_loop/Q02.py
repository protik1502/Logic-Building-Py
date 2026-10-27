# Print numbers from user input down to 1 in reverse order.

user_input = int(input("Enter your number: "))
if user_input > 0 :
    for i in range(user_input,0,-1):
        print(i,end=" ")
else:
    print("Enter the number greater than zero.")