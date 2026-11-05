# Search for a specific number in a list of inputs, and terminate the loop immediately when the number is found.

list1 = [1,32,45,7,7,4,6,87,98]
number = 6
for i in list1:
    if i == number:
        break
    else:
        print(i,end=" ")

