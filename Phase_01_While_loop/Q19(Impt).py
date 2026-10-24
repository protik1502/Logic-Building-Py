#  Print the Fibonacci series up to n terms.

user_input = int(input("Enter your number: "))
def fibonacci_series (num):
    first = 0
    second = 1
    count = 1
    if num > 0:
        print (f"Fibonacci series upto {num} terms are:")
        while num >= count :
            print (first,end=" ")
            next = first + second
            first = second
            second = next
            count += 1
    else:
        print("Enter number greater than 1")
fibonacci_series(user_input)

'''
The Fibonacci series is a sequence of numbers where each
number is the sum of the two numbers that come before it.


How It Works:

You build the sequence by adding the previous two numbers together:
• (0 + 1 = 1)
• (1 + 1 = 2)
• (1 + 2 = 3)
• (2 + 3 = 5)
• (3 + 5 = 8)

'''

        

      
