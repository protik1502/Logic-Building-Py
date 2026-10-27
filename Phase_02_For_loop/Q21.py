# Find and print the sum of all odd numbers from 1 up to n.

user_input = abs(int(input("Enter your number: ")))
sum_of_all = 0
for i in range (1,user_input + 1,2):
    sum_of_all += i
print("Sum of all the odd numbers :",sum_of_all)