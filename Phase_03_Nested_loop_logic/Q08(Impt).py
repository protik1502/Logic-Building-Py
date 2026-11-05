#  Print all Pythagorean triplets whose values are less than or equal to n.

user_input = int(input("Enter your number: "))
for i in range (1,user_input + 1):
    for j in range (1,user_input + 1):
        for k in range (1,user_input + 1):
            if i ** 2 + j ** 2 == k ** 2:
                print(f"{k ** 2} + {j ** 2} = {i ** 2} -> ({i},{j},{k})")
