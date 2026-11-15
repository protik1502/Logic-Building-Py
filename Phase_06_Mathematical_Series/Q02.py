# Find and print the sum of the first n even numbers.

def even_sun ():
    user_input = int(input("Enter your number : "))
    if user_input > 0 :
        print("Sum of even numbers :",sum(i for i in range (2,user_input + 1,2)))
    else:
        print("Enter the number greater than zero.")
even_sun()