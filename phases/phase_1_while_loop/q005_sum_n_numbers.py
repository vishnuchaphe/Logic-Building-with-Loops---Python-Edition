"""
Question 005: Sum of First n Natural Numbers
Difficulty: Beginner | Time: 10 minutes

Example:
n = 5 → 1+2+3+4+5 = 15
n = 10 → 1+2+...+10 = 55
"""

def sum_natural():
    n = int(input("Enter n: "))
    sum_value = 0
    i = 1
    while i <= n:
        sum_value += i
        i += 1
    print(f"Sum of first {n} numbers = {sum_value}")
    
    # Alternative using formula (O(1))
    # sum_formula = n * (n + 1) // 2
    # print(f"Using formula = {sum_formula}")

if __name__ == "__main__":
    sum_natural()