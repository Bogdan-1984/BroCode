# indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

"""credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")"""

# --------------------------------------------------------------------------------------------------------
# Reverse the credit number string and print.
# Leaving START and END empty and assigning a STEP as -1 (negative), will reverse the order during print.

credit_number = "1234-5678-9012-3456"

credit_number = credit_number[::-1]

print(credit_number) # => 6543-2109-8765-4321