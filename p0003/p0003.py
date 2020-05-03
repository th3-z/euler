from math import sqrt, floor

def is_prime(n):
    # No primes < 2
    if n < 2:
        return False

    # 2 is the only even prime
    if n % 2 == 0:
        return n == 2
    
    # Can't be divisble by anything larger than it's square root
    root = floor(sqrt(n))
    
    # Skip even numbers, odd numbers aren't divisible by even numbers
    for i in range(3, root, 2):
        if (n % i == 0):
            # Divisor found
            return False
    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def prime_factors(p):
    if p < 0:
        return []
    
    out = []
    limit = floor(sqrt(p))
    q = 2
    while q <= limit:
        if p % q == 0:
            out.append(q)
            p = p / q
        q = next_prime(q)
    return out


if __name__ == "__main__":
    print(max(prime_factors(600851475143)))
