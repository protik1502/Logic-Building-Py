# Count and print the number of digits in the given number.

user_input = abs(int(input("Enter your number : ")))
count = 0
if user_input == 0:
    count += 1
else:
    while True:
        a = user_input % 10
        b = user_input // 10
        user_input = b
        if a == 0:
            break
        count += 1
print(f"Number of digit : {count}")

