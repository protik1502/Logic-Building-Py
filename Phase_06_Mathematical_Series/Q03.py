# Find and print the sum of the first n odd numbers.

def odd_sum ():
        user_input = int(input("Enter your number : "))
        if user_input > 0:
            print("Sum of the odd numbers are:",sum(i for i in range (1,user_input + 1 ,2)))
        else:
              print("Enter number greater than 0")
odd_sum()