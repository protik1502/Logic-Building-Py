# Check whether the given number is an Armstrong number.

def armstrong_num (n):
    digits = len(str(n))
    original_num = n
    copy_original =original_num
    total_sum = 0
    while True:
        num1 = original_num % 10
        num2 = original_num // 10
        total_sum += num1 ** digits
        original_num = num2
        if original_num == 0:
            break
    if total_sum == copy_original:
        print(f"{copy_original} is an Armstrong number")
    else:
        print(f"{copy_original} is not an Armstrong number")
user_number = abs(int(input("Enter your number: ")))
armstrong_num(user_number)
