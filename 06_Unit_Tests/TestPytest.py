
import pytest


# 1. Functions to test
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def calculate_square(number):
    return number ** 2


# 2. Basic assertions
def test_add():
    assert add(2, 3) == 5


def test_square():
    assert calculate_square(4) == 16


# 3. Testing comparisons
def test_comparisons():
    assert 10 > 5
    assert "python".upper() == "PYTHON"
    assert 2 in [1, 2, 3]


# 4. Testing exceptions
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# 5. Using a fixture
@pytest.fixture
def numbers():
    return [10, 20, 30]


def test_sum(numbers):
    assert sum(numbers) == 60


def test_length(numbers):
    assert len(numbers) == 3


# 6. Parameterized testing
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected
