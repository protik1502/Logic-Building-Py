# Find and print the sum of the Fibonacci series up to the required number of terms.

def fibonacci ():
    first_num = 0
    second_num = 1
    terms = int(input("Enter the number of terms:"))
    total_num = 0
    for i in range (1,terms + 1):
        next_num = first_num + second_num
        total_num += first_num
        first_num = second_num
        second_num = next_num
    print(f"Sum of fibonacci series {total_num}")
fibonacci()