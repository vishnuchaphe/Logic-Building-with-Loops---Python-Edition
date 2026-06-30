"""
Question 09: Check Armstrong Number
Difficulty: Intermediate | Time: 15 minutes

Armstrong Number: Sum of digits raised to power of
number of digits = original number
Example: 153 = 1³ + 5³ + 3³ = 153 ✓
"""

def check_armstrong():
    n = int(input("Enter a number: "))
    original = n
    num_digits = 0
    temp = n
    sum_power = 0
    
    # Count digits
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    # Calculate sum of powers
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_power += digit ** num_digits
        temp //= 10
    
    if sum_power == original:
        print(f"{n} is an Armstrong Number")
    else:
        print(f"{n} is not an Armstrong Number")

if __name__ == "__main__":
    check_armstrong()