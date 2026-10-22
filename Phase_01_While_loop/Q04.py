# Print all the odd numbers from 1 to user input.

user_input = int(input("Enter the number: "))
def odd_numbers (num):
    count = 1
    while count <= num :
        if count % 2 != 0:
            print(count)
        count += 1
odd_numbers(user_input)