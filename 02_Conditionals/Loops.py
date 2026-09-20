# Loops


# 1. For Loop
for i in range(1, 6):
    print("For:", i)


# 2. For-Each Style Loop
languages = ["Python", "Java", "C++"]

for language in languages:
    print("Language:", language)


# 3. While Loop
i = 1

while i <= 5:
    print("While:", i)
    i += 1


# 4. Do-While Style Loop
while True:
    number = int(input("Enter a positive number: "))
    
    if number > 0:
        break

    print("Please enter a positive number.")


# 5. Break
for i in range(1, 6):
    if i == 3:
        break

    print("Break:", i)


# 6. Continue
for i in range(1, 6):
    if i == 3:
        continue

    print("Continue:", i)


# 7. Pass
for i in range(5):
    pass

print("Pass completed")


# 8. Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 9. Loop with Else
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")


# 10. Loop with Break and Else
for i in range(1, 5):
    if i == 3:
        break

    print(i)
else:
    print("Loop completed")