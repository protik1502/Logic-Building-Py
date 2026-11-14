# Keep taking numbers from the user until 0 is entered, then print the sum of all entered numbers. 

sum_of_all_input = 0
while True:
    user_input = int(input("Enter your number: "))
    sum_of_all_input += user_input
    if user_input == 0:
        break
print(f"Sum of all the entered numbers  : {sum_of_all_input}")
