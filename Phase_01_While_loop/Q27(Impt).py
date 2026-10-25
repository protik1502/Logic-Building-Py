# Find the LCM (Least Common Multiple) of two given numbers.

first_num = int(input("Enter your first num : ")) 
second_num = int(input("Enter your second num : "))
def lcm (num1,num2):
    if num1 > 0 and num2 > 0:
        while num2 != 0:
            reminder = num1 % num2
            num1,num2 = num2,reminder
        print(f"The LCM of {first_num} and {second_num} is {int((first_num*second_num)/num1)}")
    else:   
        print("Enter both the numbers greater than 0") 
lcm(first_num,second_num) 

'''
# Understanding LCM (Lowest Common Multiple) Logic

The **LCM** of two numbers is the smallest positive integer that is perfectly divisible by both numbers. 

---

## 🛠️ Implementation Methods

### 1. The GCD Formula Method (Recommended)
This is the most efficient approach. It uses the fundamental mathematical relationship between GCD and LCM.

*   **Logic:** LCM(a, b) = (a * b) / GCD(a, b)
*   **Formula:** To prevent large number overflow in languages like C++ or Java, divide first, 
      then multiply: (a / GCD(a, b)) * b

#### Tracing `lcm(48, 18)` Step-by-Step:
1. Find the GCD of 48 and 18, which is 6.
2. Divide 48 by 6 to get 8.
3. Multiply 8 by 18 to get 144.
4. **The LCM is 144**

'''