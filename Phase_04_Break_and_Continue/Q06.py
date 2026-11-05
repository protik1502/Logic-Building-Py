# Skip all odd numbers and print only the even numbers.

starting_num  = int(input("Enter your starting number : "))
stopping_num  = int(input("Enter your stopping number : "))
for i in range (starting_num,stopping_num + 1):
    if i % 2 != 0:
        continue
    print(i,end=" ")