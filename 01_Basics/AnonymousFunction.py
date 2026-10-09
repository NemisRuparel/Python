# Python Anonymous Functions (lambda)

# 1. Basic lambda function
square = lambda x: x * x
print("Square:", square(5))


# 2. Lambda with multiple arguments
add = lambda a, b: a + b
print("Sum:", add(10, 20))

multiply = lambda a, b: a * b
print("Product:", multiply(4, 5))


# 3. Lambda with a conditional expression
check_even = lambda number: "Even" if number % 2 == 0 else "Odd"
print("8 is:", check_even(8))
print("7 is:", check_even(7))


# 4. Lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


# 5. Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# 6. Lambda with sorted()
students = [
    ("Amit", 85),
    ("Neha", 92),
    ("Raj", 78)
]

students.sort(key=lambda student: student[1])
print("Sorted by marks (ascending):", students)

students.sort(key=lambda student: student[1], reverse=True)
print("Sorted by marks (descending):", students)


# 7. Equivalent regular function
def calculate_cube(number):
    return number ** 3


cube = lambda number: number ** 3

print("Cube using def:", calculate_cube(3))
print("Cube using lambda:", cube(3))
