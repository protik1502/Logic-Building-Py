# Print the square of each number from 1 to n. 

user_input = int(input("Enter your num: "))
def square(num):
    if num > 0 :
        count = 1 
        while num >= count:
            print(f"Square of {count} is {count**2}")
            count += 1
    else:
        print("Enter the number greater than 0")
square(user_input)
