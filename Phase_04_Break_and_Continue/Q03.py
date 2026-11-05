# Take 5 numbers as input, skip any number that is 0 using continue, and calculate the sum of the remaining numbers.

number = [1,0,4,6,7]
sum_of_all = 0
for i in number:
    if i == 0:
        continue
    else:
        sum_of_all += i
print(f"Sum of all the numbers = {sum_of_all}")
