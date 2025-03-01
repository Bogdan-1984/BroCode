# Typecasting = the process of converting a variable from one data type to another.
#           str(), int(), float(),bool()

name = "Jerel"  # string
age = 25  # int
gpa = 3.2  # float
is_student = True  # bool

# type(name) = will not show any results
# print(type(is_student)) => CORRECT way of writing

'''gpa = int(gpa)
print(gpa)'''
# RESULT: will truncate the decimal portion, will print (3) instead of (3.2)


'''age = float(age)
print(age)'''
# RESULTS: will display (25.0) instead of (25)

# It's like taking the number 25 [int], and enclosing it into quotes, "25" [str]
'''age = str(age)'''

# Will still display 25, like a [int], but in fact it's a [str].
'''print(age)'''

# Will show the class type of age, [str]
'''print(type(age))'''


# name = bool(name)
# print(name)
# RESULT: as long as srt has a value written, the result will be TRUE. If str has no values added,
#        the print result will state FALSE.
