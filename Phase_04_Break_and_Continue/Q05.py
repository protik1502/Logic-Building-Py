# Keep taking numbers from the user and print them until a negative number appears, then stop the loop. 

while True:
    user_input = int(input("Enter your number : "))
    if user_input < 0 :
        break
    print(user_input)