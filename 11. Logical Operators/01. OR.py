# Logical operators = evaluate multiple condition (or, and, not)
#               or = at least one condition must be True
#               and = both condition must be True
#               not = inverts the condition (not True, not false)

temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
