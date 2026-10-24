# Check whether the given number is a prime number.

user_input = int(input("Enter your number: "))
def prime_num(num):
    if num > 1:
        is_prime = True
        count = 2
        while num >= count * count:
            if num % count == 0:
                is_prime = False

            count += 1

        if is_prime :
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    else:
        print("Enter number greater than 1.")
prime_num(user_input)