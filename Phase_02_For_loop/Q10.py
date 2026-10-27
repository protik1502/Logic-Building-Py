# Print the Fibonacci series up to the required number of terms.

user_input = int(input("Enter the number of terms: "))
def fibonacci (num):
    first_num = 0
    second_num = 1
    for i in range(0,num):
        print(first_num,end=" ")  
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
fibonacci(user_input)