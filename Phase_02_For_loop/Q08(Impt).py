#  Print all prime numbers between 1 and user input.

user_input = int(input("Enter your number : "))
def prime_num (num):
    if num < 2:
        print("Enter number greater than 1")
        return
    print (f" The prime numbers between 1 and {num} are:")
    for i in range (2,num + 1):
        prime = True
        for divisor in range(2,i) :
            if i % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            print(i,end=" ")
prime_num(user_input)