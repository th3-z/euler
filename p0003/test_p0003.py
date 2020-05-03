from p0003 import prime_factors, is_prime, next_prime

def test_prime_factors():
    assert len(prime_factors(0)) == 0
    assert len(prime_factors(1)) == 0
    assert len(prime_factors(-1)) == 0
    assert max(prime_factors(600851475143)) == 6857
    assert sum(prime_factors(13195)) == 5 + 7 + 13 + 29

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(6857)
    assert is_prime(next_prime(600851475143))
    assert not is_prime(1)
    assert not is_prime(0)
    assert not is_prime(-1)

def test_next_prime():
    assert next_prime(-7) == 2
    assert next_prime(0) == 2
    assert next_prime(1) == 2
    assert next_prime(5) == 7
    assert next_prime(878663) == 878677
