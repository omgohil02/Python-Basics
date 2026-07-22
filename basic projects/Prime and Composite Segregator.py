#Prime and Composites Segregator in python

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Enter 10 whole numbers:")
numbers = []

try:
    for i in range(10):
        val = int(input("> "))
        # Validate that all inputs are positive integers (> 0)
        if val <= 0:
            print("Error: Input must be a positive integer.")
            exit()
        numbers.append(val)
        
    primes = []
    composites = []

    for num in numbers:
        if num > 1:
            if is_prime(num):
                primes.append(num)
            else:
                composites.append(num)

    # Sort in ascending order
    primes.sort()
    composites.sort()

    print(f"Prime numbers in ascending order: {primes}")
    print(f"Composite numbers in ascending order: {composites}")
    print(f"Count of prime numbers: {len(primes)}")
    print(f"Count of composite numbers: {len(composites)}")

except ValueError:
    print("Error: Invalid input. Please enter whole numbers only.")