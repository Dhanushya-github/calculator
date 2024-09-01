try:
    x = input("Type a number: ")
except EOFError:
    print("No input received. Using default value.")
    x = 0  # or any default value you prefer
print("The number is: {x}")
