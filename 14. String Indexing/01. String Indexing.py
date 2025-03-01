# indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

# The running index is inclusive, always shows in the print
# The ending index is exclusive, meaning it's not taken into account when running the print
# print(credit_number[0:4]) would normally prin [1,2,3,4,-] but because the ending index is exclusive, [-] is shown.

credit_number = "1234-5678-9012-3456"

# print(credit_number[4]) # --> prints 4th character
# print(credit_number[0:4]) # --> prints from the 1st character up to the 4th.
#                               ex: 1234
# print(credit_number[5:9]) # ---> same as above
# print(credit_number[5:]) # ---> prints starting from the 5th character until the END.
#                               ex: 5678-9012-3456
# print(credit_number[-1]) # ---> prints the last nr in the sequence. In this case, it's the last 6

# print(credit_number[::2]) # --> prints the 2nd character in sequence. ex: 13-6891-46
# print(credit_number[::3]) # --> prints the 3rd character, ex: 146-136