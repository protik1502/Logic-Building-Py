# Print the multiplication table of a given number.

user_input = int(input("Enter your number : "))
count = 1
while True:
    print(f"{user_input} x {count} = {user_input * count}")
    if count == 10:
        break
    count += 1
