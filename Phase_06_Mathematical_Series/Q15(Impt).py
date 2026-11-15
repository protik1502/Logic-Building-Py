#  Check whether the given number is a Strong number, where the number equals the sum of factorials of its digits

user_input = int(input("Enter your number : "))
copy_user = user_input
sum_of_all = 0
while user_input != 0:
    a = user_input % 10
    user_input = user_input // 10
    factorial = 1
    for i in range (1,a + 1):
        factorial *= i
    sum_of_all += factorial
if sum_of_all == copy_user:
    print(f"{copy_user} is a strong number.")
else:
    print(f"{copy_user} is not a strong number.")

    