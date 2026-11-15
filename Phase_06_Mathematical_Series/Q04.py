# Print the first n terms of an arithmetic progression for the given first term and common difference. 

first_term = abs(int(input("Enter your first term: ")))
common_diff = abs(int(input("Enter your common difference: ")))
num_term = abs(int(input("Enter the number of terms: ")))
for i in range (1,num_term + 1):
    print(first_term,end=" ")
    first_term += common_diff
