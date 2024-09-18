pattern_size = int(input("Enter the size of the pattern: "))

# Draw the Pattern using while loops
i = 0
while i < pattern_size:  # Outer loop for rows
    j = 0
    while j < pattern_size:  # Inner loop for columns
        print("*", end="")
        j += 1
    print()  # Move to the next line after printing each row
    i += 1
