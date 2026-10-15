# Conditionals

# 1. If Statement
age = 20

if age >= 18:
    print("You are an adult")


# 2. If-Else Statement
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# 3. If-Elif-Else Statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Nested If
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")


# 5. Conditional Expression
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# 6. Multiple Conditions
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")


# 7. Practical Program
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")