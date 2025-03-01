# Nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

# Outer loop runs 3 times, creating 3 rows of numbers
for x in range(rows):
    # Inner loop runs from 1 to 9, printing numbers on the same line
    for y in range(columns):
        print(symbol, end="")  # Print numbers 1 to 9 on the same line without a newline
    print()  # Move to the next line after printing the sequence 1 to 9
