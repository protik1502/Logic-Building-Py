# Create a menu-driven program that allows the user to choose and perform different operations.

choices = [1,2,3,4,0]
first = 20
second = 5
choice = 0
index = 0
while True:
    choice = choices[index]
    index += 1
    if choice == 1:
        print(f"Addition = {first + second}")
    elif choice == 2 :
        print(f"Substraction = {first - second}")
    elif choice == 3:
        print(f"Multiplication = {first * second}")
    elif choice == 4 :
        print(f"Division = {int(first / second)}")
    elif choice == 0:
        print("Exit programm")
    else:
        print("Invalid input.")
    if choice == 0:
        break


