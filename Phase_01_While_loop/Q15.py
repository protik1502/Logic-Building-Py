# Check whether the given number is an Armstrong number.

user_input = int(input("Enter your number: "))
def armstrong_number (num):
    num = abs(num)
    original_num = num
    count = len(str(num))
    sum_of_num = 0
    while num > 0:
        rev = num % 10
        num = num // 10
        sum_of_num = sum_of_num + rev**count
    if original_num == sum_of_num:
        return "The number is Armstrong number"
    else:
        return "The number is not Armstrong number"
print(armstrong_number(user_input))

'''
 Even the negative inputs will be compared by making them positive.
 An Armstrong number (also known as a narcissistic number or pluperfect number)
 is a number that equals the sum of its own digits, where each digit is raised 
 to the power of the total number of digits.
 For example:
 3-digit numbers: 153 is an Armstrong number because it has 3 digits and 
 (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153). Other 3-digit examples include 370, 371, and 407.     
 '''