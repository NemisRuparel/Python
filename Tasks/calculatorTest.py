from calculator import square, square_faulty

def test_square():
    assert square(5) == 25
    assert square(-3) == 9
    assert square(0) == 0

def test_square_faulty():
    assert square_faulty(5) == 25
    assert square_faulty(-3) == 9
    assert square_faulty(0) == 0

