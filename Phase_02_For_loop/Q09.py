# Check whether the given number is a prime number.

user_input = int(input("Enter your number: "))
def prime_num (num):
    if num < 2:
        print("Enter the number greater than 1")
        return
    for divisor in range (2,num):
        if num % divisor == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is prime number.")
prime_num(user_input)

'''
In Python, the statement for i in range(2, 2): creates an empty loop that will never execute.

Why it happens

The range(start, stop) function generates integers starting at start up to, butgenerates an empty sequence.  excluding, the stop value. 
Because the start value (2) is already equal to the exclusive stop value (2), the function 
As a result, the loop terminates immediately without running any code inside it.

# The loop sequence is empty, so the print statement is completely skipped
for i in range(2, 2):
    print(f"Loop running: i is {i}")

print("Loop finished!") 
# Output: Loop finished!

'''