"""
Question 008: Check if Number is Palindrome
Difficulty: Beginner | Time: 12 minutes

Example:
n = 121 → Palindrome
n = 123 → Not Palindrome
"""

def check_palindrome():
    n = int(input("Enter a number: "))
    original = abs(n)
    reverse = 0
    temp = original
    
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    
    if original == reverse:
        print(f"{n} is a Palindrome")
    else:
        print(f"{n} is not a Palindrome")

if __name__ == "__main__":
    check_palindrome()