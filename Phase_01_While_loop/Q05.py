# Print multiplication table from n x 1 to n x 10.

user_input = int(input("Enter the number for multiplication table: "))
def multiplication_table (num):
    count = 1
    while count <= 10:
        print(f"{num} x {count} = {num * count}")
        count += 1
multiplication_table(user_input)