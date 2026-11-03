from calculator import square, cube

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_cube():
    assert cube(2) == 8
    assert cube(-2) == -8