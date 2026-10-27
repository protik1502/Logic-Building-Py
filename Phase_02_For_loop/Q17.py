# Print the cube of each number from 1 to n.

user_input = int(input("Enter your number: "))
def square_num (num):
    num = abs(num)
    if num == 0:
        print(f"Enter the number greater than {num}")
    else:
        for i in range(1,num + 1):
            print(f"The cube of {i} is {i ** 3}")
square_num(user_input)