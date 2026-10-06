# Exceptions

# 1. Handling ZeroDivisionError
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")


# 2. try-except-else
try:
    number = int(input("Enter another number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Result:", result)


# 3. finally
try:
    print("Executing try block")

except Exception:
    print("An error occurred.")

finally:
    print("Finally block executed.")


# 4. Raising an Exception
age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as error:
    print("Error:", error)


# 5. Custom Exception
class AgeError(Exception):
    pass


try:
    age = 15

    if age < 18:
        raise AgeError("Age must be 18 or above.")

except AgeError as error:
    print("Custom Error:", error)