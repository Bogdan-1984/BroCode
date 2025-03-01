# Nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# Outer loop runs 3 times, creating 3 rows of numbers
for x in range(3):
    # Inner loop runs from 1 to 9, printing numbers on the same line
    for y in range(1, 10):
        print(y, end="")  # Print numbers 1 to 9 on the same line without a newline
    print()  # Move to the next line after printing the sequence 1 to 9
