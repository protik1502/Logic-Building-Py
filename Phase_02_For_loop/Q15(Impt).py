# Find the LCM (Least Common Multiple) of the given numbers.

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
def lcm (num1,num2):
    large_num = max(num1,num2)
    small_num = min(num2,num1)
    absolute_lcm = small_num * large_num
    for i in range (large_num,absolute_lcm +1,large_num):
        if i % small_num == 0:
            print(f"The LCM of {small_num} and {large_num} is {i}.")
            break
lcm(first_number,second_number)

'''
Here is the simplified logic:
• Find the largest: Identify the larger and smaller of the two numbers.
• Count by the largest: Loop through the multiples of the larger number (e.g., if it's 6, check 6, 12, 18...).
• Test for divisibility: Check if the smaller number divides into the current multiple perfectly with no remainder.
• Stop at the first match: The very first number that passes the test is your LCM.
'''
