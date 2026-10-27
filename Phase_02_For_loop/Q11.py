# Find and print the sum of the Fibonacci series.

user_input = int(input("Enter the number of terms: "))
def fibonacci (num):
    num = abs(num)
    first_num = 0
    second_num = 1
    sum_of_all = 0
    for i in range(0,num):
        sum_of_all += first_num
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
    print(f"Sum of the Fibonacci Series upto {num}th term = {sum_of_all}")  
fibonacci(user_input)