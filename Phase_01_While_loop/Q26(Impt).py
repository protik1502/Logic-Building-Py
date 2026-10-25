# Find the HCF (Highest Common Factor) of two given numbers.

first_num = int(input("Enter your first number: "))
copy_first_num  = first_num
second_num = int(input("Enter your second number: "))
copy_second_num  = second_num
if first_num > 0 and second_num > 0:
    while first_num != 0:
        remainder = second_num % first_num
        second_num = first_num
        first_num = remainder
    print(f"HCF of {copy_first_num} and {copy_second_num} is {second_num} ")
else:
    print("Enter both the numbers greater than 1")


'''
# Understanding GCD (Greatest Common Divisor) Logic

The **GCD** (also known as HCF - Highest Common Factor) of two numbers is the largest positive 
integer that divides both numbers completely without leaving a remainder.

---

## 🛠️ Implementation Methods

### 1. The Euclidean Algorithm (Recommended)
       This is the most efficient approach. It relies on the principle that the GCD of two numbers 
       also divides their difference or the remainder of their division.

*   **Logic:** gcd(a, b) = gcd(b, a % b)
*   **Process:** Keep replacing a with b and b with a % b until b becomes 0. The remaining a is your GCD.

#### Tracing gcd(48, 18) Step-by-Step:
1. 48 % 18 = 12 -> Next step: gcd(18, 12)
2. 18 % 12 = 6  -> Next step: gcd(12, 6)
3. 12 % 6 = 0   -> Next step: gcd(6, 0)
4. **b is now 0 -> The GCD is 6**

### 2. The Subtraction Method :
       An older variation of the Euclidean algorithm that replaces division with repeated subtraction.

*   **Logic:** Subtract the smaller number from the larger number.
*   **Process:** Loop while a != b. If a > b , do a = a - b. Otherwise, do b = b - a . 
      When they become equal, that value is the GCD.

'''