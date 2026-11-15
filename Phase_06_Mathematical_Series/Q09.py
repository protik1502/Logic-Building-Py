# Calculate and print the value of the series 1³ + 2³ + 3³ + … + n³

user_input = int(input("Enter your number : "))
value = 0
for i in range(1,user_input + 1):
    value += i ** 3
print(f"The sum of the series {value}")