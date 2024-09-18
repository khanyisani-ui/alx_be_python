pattern_size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
for i in range(pattern_size):  # Outer loop for rows
    for j in range(pattern_size):  # Inner loop for columns
        print("*", end="")
    print()  # Move to the next line after printing each row
