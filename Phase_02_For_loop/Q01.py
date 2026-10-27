# Print all numbers from 1 to user input.

user_input = int(input("Enter your number: "))
if user_input > 0:
    for i in range(1,user_input + 1):
        print(i,end=" ")
else:
    print ("Enter number greater than 0")