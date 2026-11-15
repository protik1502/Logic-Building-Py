# Find and print the sum of the first n natural numbers.

def natural_sum ():
    user_input = int(input("Enter your number : "))
    if user_input > 0:
        print("Sum of all the natural  numbers :",sum(i for i in range(1,user_input + 1)))
    else:
        print("Enter the greater than zero.")
natural_sum()