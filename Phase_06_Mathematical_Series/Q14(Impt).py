# Calculate and print the value of the series x − x²/2! + x³/3! − x⁴/4! + …..

user_input = int(input("Enter your number: "))
n = int(input("Enter the number of terms : "))
factorial = 1
sum_of_all = 0
for i in range(1,n + 1):
    factorial *= i
    term = i ** i / factorial
    if i % 2 == 0:
        sum_of_all -= term
    else:
        sum_of_all += term
print("Final result :",sum_of_all)


    
