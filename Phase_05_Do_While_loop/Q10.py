# Print the Fibonacci series up to the required number of terms.

def fibonacci(n):
    count = 1
    first_num = 0
    second_num = 1
    while True:
        print(first_num,end=" ")
        next_num = first_num + second_num
        first_num,second_num = second_num,next_num
        count += 1
        if n < count:
            break
user_input = abs(int(input("Enter your number: ")))
fibonacci(user_input)