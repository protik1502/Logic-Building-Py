# Find and print the sum of the Fibonacci series up to n terms. 

user_input = int(input("Enter your number: "))
def sum_of_fibonacci_series (num):
    if num > 0:
        first_num = 0
        second_num = 1
        total_sum = 0
        count = 1
        
        while num >= count:
            total_sum = total_sum + first_num
            third_num = first_num + second_num
            first_num = second_num
            second_num = third_num
            count += 1
        print(f"Sum of all the numbers upto {num} terms are: {total_sum}")
    else:
        print("Enter number greater than 1")
sum_of_fibonacci_series(user_input)
