# Print all prime numbers up to n using nested loop checking.

user_input = abs(int(input("Enter your number: ")))
for i in range(2,user_input + 1):
    prime_num = True
    for j in range(2,i):
        if i % j == 0:
            prime_num = False
            break
    if prime_num:
        print(f"The number {i} is a prime number.")