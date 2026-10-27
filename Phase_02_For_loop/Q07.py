# Calculate and print the factorial of every number from 1 to n. 

user_input = int(input("Enter your number : "))
def sum_of_all (num):
    start = 1
    if num == 0:
        print(f"The factorial of {num} is {start}.")
    elif num > 0:
        for i in range (start,num + 1):
            start = start * i
            print(f"The factorial of {i} is {start}")
sum_of_all(user_input)
        