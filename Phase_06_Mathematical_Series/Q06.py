# Print the Fibonacci series up to the required number of terms.

def fibonacci():
    first_num = 0
    second_num = 1
    terms = int(input("Enter the number of terms: "))
    for i in range(1,terms + 1):
        print(first_num,end=" ")
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num
fibonacci()