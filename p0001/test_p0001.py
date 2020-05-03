from p0001 import mult35range

def test_mult35range():
    assert sum(mult35range(0,1000)) == 233168
    assert sum(mult35range(99,100)) == 99
    assert sum(mult35range(0,100)) == 2318
    assert sum(mult35range(0,1)) == 0
