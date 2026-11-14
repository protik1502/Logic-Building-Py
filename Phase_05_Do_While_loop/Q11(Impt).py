# Find the HCF (Highest Common Factor) of the given numbers.

first_num = abs(int(input("Enter your first number : ")))
second_num = abs(int(input("Enter your second number : ")))
min_num = min(first_num,second_num)
max_number = max(first_num,second_num)
step = min_num
while True:
    if max_number % step == 0 and min_num % step == 0:
        print(f"The HCF of {min_num} and {max_number} is {step}")
        break
    else:
        step -= 1
