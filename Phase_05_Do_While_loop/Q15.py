# Calculate and print the sum of even digits and the sum of odd digits of the given number separately.

user_input = int(input("Enter your number: "))
even_sum = 0
odd_sum = 0
while True:
    digit = user_input % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    user_input = user_input // 10
    if user_input == 0 :
        break
print(f"Sum of even numbers are {even_sum}")
print(f"Sum of odd numbers are {odd_sum}")
