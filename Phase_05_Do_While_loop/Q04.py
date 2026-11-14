# Keep taking numbers from the user until 0 is entered, then print the largest number among all inputs.

entered_numbers = []
while True:
    user_input = int(input("Enter your number : "))
    entered_numbers.append(user_input)
    if user_input == 0:
        break
print(f"Largest number : {max(entered_numbers)}")