#  Print the Fibonacci pattern row by row, where each row prints the next Fibonacci numbers.

user_input = abs(int(input("Enter the number of rows: ")))
first_num = 0
second_num = 1
for i in range (1,user_input + 1):
    for j in range (1,user_input + 1):
        print(first_num, end= " ")
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
    print()
