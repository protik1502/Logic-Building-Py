# Calculate and print the value of the series 1² + 2² + 3² + … + n²

user_input = int(input("Enter your number : "))
value = 0
for i in range(1,user_input + 1):
    value += i ** 2
print(f"The sum of the series {value}")