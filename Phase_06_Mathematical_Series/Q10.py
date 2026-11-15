#  Calculate and print the value of the series 1 + 1/2 + 1/3 + … + 1/n

user_input = int(input("Enter your number : "))
value = 0
for i in range(1,user_input + 1):
    value += 1 / i
print(f"The sum of the series {value}")