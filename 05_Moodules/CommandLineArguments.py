# Command-Line Arguments
import sys

# Display all command-line arguments
print("Arguments:", sys.argv)

# Check whether the required arguments are provided
if len(sys.argv) < 3:
    print("Usage: python command-line-arguments.py <name> <age>")
    sys.exit(1)

# Access arguments
name = sys.argv[1]
age = int(sys.argv[2])

# Display values
print("Name:", name)
print("Age:", age)