# Python assert Keyword
# Demonstrates assertions with conditions, messages, and functions.

# 1. Basic assertion
age = 20

assert age >= 18
print("Age assertion passed.")


# 2. Assertion with a custom message
marks = 75

assert marks >= 35, "Student has failed the exam."
print("Marks assertion passed.")


# 3. Assertion inside a function
def calculate_square(number):
    assert isinstance(number, (int, float)), "Number must be numeric."
    return number ** 2


result = calculate_square(5)
print("Square:", result)


# 4. Assertion with a false condition
value = -10

try:
    assert value >= 0, "Value must be non-negative."
except AssertionError as error:
    print("Assertion failed:", error)


# 5. Essential validation using ValueError
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


try:
    validate_age(-5)
except ValueError as error:
    print("Validation error:", error)