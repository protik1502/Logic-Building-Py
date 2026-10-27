# Find and print the sum of the first n natural numbers.

number = int(input("Enter your number: "))
sum_of_all = 0
if number > 0:
    for i in range(1,number + 1):
        sum_of_all += i
    print("Sum of all the natural numbers:",sum_of_all)
else:
    print("Enter the number greater than 0.")
