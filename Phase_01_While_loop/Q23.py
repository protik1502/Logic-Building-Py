# Print all numbers between a and b that are divisible by 7.


a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
def divisible_by_seven(num1,num2):
    if num1 > 0 and num1 < num2:
        while num1 < num2:
            if num1 % 7 == 0:
                print(num1,end=" ")
            num1 += 1
    else:
        print("ENter valid numbers")
divisible_by_seven(a,b)