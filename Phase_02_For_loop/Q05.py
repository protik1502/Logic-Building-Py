#  Print the multiplication table of a given number. 

user_input = int(input("Enter your number : "))
def multiplication (num):
    num = abs(num)
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
multiplication(user_input)
