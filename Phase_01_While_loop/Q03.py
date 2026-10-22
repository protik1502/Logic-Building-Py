# Print all the even numbers between 1 to user input numbers.


def even_number (num):
    count = 1
    while count <= num:
        if count % 2 == 0:
            print(count)
        count+=1
user_input = int(input("Enter your number: "))
even_number(user_input)