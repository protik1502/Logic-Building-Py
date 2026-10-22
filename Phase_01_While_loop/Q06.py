# Calculate and print the sum of n natural numbers.

natural_numbers = int(input("Enter the your number: "))
def add_natural_numbers (num):
    count = 1
    sum = 0
    if num > 0:
        while count <= num:
            sum = sum + count
            count += 1
        print("Sum of all the natural numbers:",sum) 
    else:
        print("Enter a valid number")  
add_natural_numbers(natural_numbers)
