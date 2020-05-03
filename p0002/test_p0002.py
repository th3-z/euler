from p0002 import fib_even

def test_fib_even():
    assert sum(fib_even(4000000)) == 4613732
    assert sum(fib_even(0)) == 0
    assert sum(fib_even(-1)) == 0
    assert sum(fib_even(2)) == 2
    assert sum(fib_even(3)) == 2
