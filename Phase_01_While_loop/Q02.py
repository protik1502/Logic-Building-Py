# Print all the numbers from user input down to 1 in reverse order.

num = int(input("Enter the number: "))
def reverse_count(a):
    while a > 0:
        print(a)
        a -= 1
reverse_count(num)
