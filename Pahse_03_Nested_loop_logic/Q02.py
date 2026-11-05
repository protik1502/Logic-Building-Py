# Print all possible pairs (i, j) where both i and j range from 1 to n. 

user_input = int(input("Enter your number : "))
for i in range(1,user_input+1):
    for j in range(1,i+1):
        print(f"{i,j}",end=" ")