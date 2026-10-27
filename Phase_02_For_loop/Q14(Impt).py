# Find the HCF (Highest Common Factor) of the given numbers.

user_input = int(input("Enter your first number : "))
user_input2 = int(input("Enter your second number : "))
def hcf (num1,num2):
    highest_factor = 1
    smaller = min(num1,num2)
    for i in range(smaller,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            highest_factor = i
            break
    print(f"The factors of {num1} and {num2} are {highest_factor}")  
hcf(user_input,user_input2)


