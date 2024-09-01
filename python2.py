import sys

if len(sys.argv) != 3:
    print("Usage: python addition.py <first_number> <second_number>")
    sys.exit(1)

try:
    first_number = float(sys.argv[1])
    second_number = float(sys.argv[2])
except ValueError:
    print("Please enter valid numbers.")
    sys.exit(1)

result = first_number + second_number
print(f"The result is: {result}")
