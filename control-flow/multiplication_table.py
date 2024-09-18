# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
for i in range(1, number + 1):
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()  # Move to a new line after each row
