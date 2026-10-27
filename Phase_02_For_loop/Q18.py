# Print all numbers between a and b that are divisible by 7.


number1 = 1
number2 = 100
def divisible_by_seven (num1,num2):
    max_num = max(num1,num2)
    min_num = min(num1,num2)
    for i in range(min_num,max_num + 1):
        if i % 7 == 0:
            print(i,end=" ")
divisible_by_seven(number1,number2)