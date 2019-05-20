from myPackage import somePython


def test_caesar():
    assert somePython.caesar('abc', 1) != 'bcd', 'something went wrong!'
