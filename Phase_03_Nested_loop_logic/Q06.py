# Generate and print a number triangle pattern using nested loops. 

user_input = abs(int(input("Enter the number of rows : ")))
for i  in range(1,user_input + 1):
    for  j in range (1,i + 1):
        print(j,end=" ")
    print()