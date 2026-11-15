# Calculate and print the value of the series 1! + 2! + 3! + … + n!.

user_input = int(input("Enter your number : "))
total_sum = 0
for i in range(1,user_input + 1):
    sum_of = 1
    for j in range (1,i + 1):
        sum_of *= j
        total_sum += sum_of
    print(sum_of,end=" ")
    if j < user_input:
        print("+",end=" ")
print("=",total_sum)