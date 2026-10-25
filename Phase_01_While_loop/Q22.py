# Print the cube of each number from 1 to n.
user_input = int(input("Enter your number: "))
def cube_number(num):
    if num > 0 :
        count = 1
        while num >= count:
            print(f"The cube of {count} is {count ** 3}")
            count += 1
    else:
        print("Enter number greater than 0")
cube_number(user_input)