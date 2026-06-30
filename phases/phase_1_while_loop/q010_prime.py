"""
Question 010: Print Prime Numbers 1 to 100
Difficulty: Intermediate | Time: 15 minutes
"""

def print_primes():
    n = 100
    num = 2
    
    while num <= n:
        is_prime = True
        i = 2
        
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        
        if is_prime:
            print(num, end=" ")
        num += 1
    print()

if __name__ == "__main__":
    print_primes()