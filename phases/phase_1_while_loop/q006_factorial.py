"""
Question 06: Factorial of a Number
Difficulty: Beginner | Time: 10 minutes

Example:
n = 5 → 5! = 5×4×3×2×1 = 120
"""

def factorial():
    n = int(input("Enter a number: "))
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(f"Factorial of {n} = {fact}")

if __name__ == "__main__":
    factorial()