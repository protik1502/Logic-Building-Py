# Find and print the sum of digits of the given number.

total_sum = 0
while True:
    user_input = int(input("Enter yuor number : "))
    if user_input < 0:
        break
    else:
        total_sum += user_input
print(f"Total sum of the given digits are {total_sum}")