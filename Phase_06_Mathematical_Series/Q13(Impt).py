# Calculate and print the value of the series 1 + x + x² + x³ + … + xⁿ.

user_input = int(input("Enter your number : "))
power = int(input("Enter the power : "))
total_sum = 0
for i in range (power + 1):
    sum_all = user_input ** i
    print(sum_all,end=" ")
    total_sum += sum_all
    if i < power:
        print("+",end=" ")
print("=",total_sum)
