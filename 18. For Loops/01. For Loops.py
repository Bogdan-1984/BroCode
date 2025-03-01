# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x) # prints from 1-12, skips everything starting with 13, up to 20

# --------------------------------------------------------------------------------------------------------------

"""for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)""" # prints all from 1 to 20, but skips nr 13

# --------------------------------------------------------------------------------------------------------------

"""for x in reversed(range(1, 11)):
    print(x)
print("Happy New Year!")""" # if range is enclosed in reversed,
                            # it will print in reverse, then prin print("Happy New Year!")

# --------------------------------------------------------------------------------------------------------------
"""x = 1
while x <= 10:
    print(x)
    x += 3"""
