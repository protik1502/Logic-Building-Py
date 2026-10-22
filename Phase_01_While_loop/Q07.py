# Calculate and Print the sum of all even even numbers from 1 to n.

user_input = int(input("Enter your number: "))
def even_sum (num):
    count = 2
    sum = 0
    if num > 1:
        while count <= num :
            sum = sum + count
            count+=2
        print("Sum of all the even numbers:",sum)
    else:
        print("Enter a valid number")
even_sum(user_input)
