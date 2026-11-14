# Keep taking numbers from the user until a negative number is entered, then count how many positive numbers were entered.

count  = 0
while True:
    user_input = int(input("Enter your number: "))
    count += 1
    if user_input < 0:
        break
print(f"Number of attempts {count}")

