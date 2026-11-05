# For every number from 1 to n, count and print the total number of its factors.
user_input = abs(int(input("Enter your number: ")))
for i in range (1,user_input + 1):
    count = 0
    for j in range(1,i + 1):
        if i % j == 0:
            count+=1
    print(f"Total number of factors of {i} are {count} ")

