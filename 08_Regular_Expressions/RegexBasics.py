
# Python Regular Expressions (Regex Basics)

import re

# 1. Search for a pattern
text = "Python is a programming language."

result = re.search(r"programming", text)
print("Search:", result.group() if result else "No match")


# 2. Match at the beginning
result = re.match(r"Python", text)
print("Match:", result.group() if result else "No match")


# 3. Match the entire string
print("Full match:", bool(re.fullmatch(r"\d+", "12345")))
print("Invalid full match:", bool(re.fullmatch(r"\d+", "123abc")))


# 4. Find all numbers
text = "My marks are 85, 90, and 78."

numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

marks = [int(number) for number in numbers]
print("Integer marks:", marks)


# 5. Common character classes
text = "Python 123"

print("Digits:", re.findall(r"\d", text))
print("Words:", re.findall(r"\w+", text))
print("Whitespace:", re.findall(r"\s", text))


# 6. Replace matching text
text = "Python 123 is easy 456"

result = re.sub(r"\d+", "#", text)
print("Substitution:", result)


# 7. Split using multiple delimiters
text = "apple,banana;orange mango"

result = re.split(r"[,;\s]+", text)
print("Split:", result)


# 8. Extract groups from a date
text = "Date: 2026-10-10"

result = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

if result:
    print("Year:", result.group(1))
    print("Month:", result.group(2))
    print("Day:", result.group(3))


# 9. Case-insensitive search
text = "Python is GREAT"

result = re.search(r"great", text, re.IGNORECASE)
print("Case-insensitive:", result.group() if result else "No match")


# 10. Extract an email-like string
text = "Contact us at support@example.com"

pattern = r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"

emails = re.findall(pattern, text)
print("Email-like strings:", emails)
