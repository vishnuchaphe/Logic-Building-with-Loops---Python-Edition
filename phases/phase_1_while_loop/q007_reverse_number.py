"""
Question 007: Reverse a Number
Difficulty: Beginner | Time: 12 minutes

Example:
n = 12345 → 54321
n = 1000 → 0001 (displays as 1)
"""

def reverse_number():
    n = int(input("Enter a number: "))
    reverse = 0
    temp = abs(n)
    
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    
    if n < 0:
        reverse = -reverse
    
    print(f"Reversed number = {reverse}")

if __name__ == "__main__":
    reverse_number()