# Print the series of powers of two: 1 + 2 + 4 + 8 + … + 2ⁿ

user_input = int(input("Enter the number of terms : "))
for i in range (user_input + 1):
    print(2 ** i ,end=" ")
    if i < user_input:
        print("+",end=" ")