# Print all prime numbers between 1 to user input.

user_input = int(input("Enter your number: "))

def prime_num (num):
    if num > 1:
        print ("The prime numbers are:",end=" ")
        count = 2
        while num >= count:
            is_prime = True
            add = 2
            while add * add <= count:
                if count % add == 0:
                    is_prime = False
                    break
                add += 1
            if is_prime:
                print(count,end=" ")
            count += 1
    else:
        print ("Enter number greater than 1")
prime_num(user_input)
