name = "Jerel"  # string
age = 25  # int
gpa = 3.2  # float
is_student = True  # bool

age = str(age)
'''age += 1'''
# TypeError: can only concatenate str (not "int") to str.
# => 25 is considered a str, while 1 is a int

'''age += "1"'''  # it becomes a str concatenation if written in quotes
# Result will be 251 (years old)

'''name = bool(name)'''
'''print(name)'''
# RESULT: as long as str has a value written, the result will be TRUE.
#         If str has no values added, the print result will state FALSE.
# Typecasting bool can be used to check if someone enters their name or not
