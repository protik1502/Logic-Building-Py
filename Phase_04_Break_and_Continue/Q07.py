# Continuously add numbers in a loop and stop the loop when the sum becomes greater than 100.

starting_num  = int(input("Enter your starting number : "))
stopping_num  = int(input("Enter your stopping number : "))
sum_of_all_number = 0
for i in range (starting_num,stopping_num + 1):
    sum_of_all_number += i
    if sum_of_all_number > 100:
        break
print(f"Sum : {sum_of_all_number}")