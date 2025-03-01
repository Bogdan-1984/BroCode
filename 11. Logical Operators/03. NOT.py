# Logical operators = evaluate multiple condition (or, and, not)
#               or = at least one condition must be True
#               and = both condition must be True
#               not = inverts the condition (not True, not false)


temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny 🌞")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny 🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside 😃")
    print("It is sunny 🌞")
if temp >= 28 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is CLOUDY 🌥️")
elif temp <= 0 and not is_sunny:
    print("It is cold outside 🥶")
    print("It is CLOUDY 🌥️")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside 😃")
    print("It is CLOUDY 🌥️")