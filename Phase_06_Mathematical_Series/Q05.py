# Print the first n terms of a geometric progression for the given first term and common ratio.

first_term = abs(int(input("Enter your first term: ")))
ratio = abs(int(input("Enter your ratio :")))
num_terms = abs(int(input("Enter the number of terms:")))
for i in range(1,num_terms + 1):
    print((first_term),end=" ")
    first_term *= ratio


