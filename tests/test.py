from myPackage import somePython


def test_caesar():
    assert somePython.caesar('abc') != 'bcd', 'something went wrong!'
