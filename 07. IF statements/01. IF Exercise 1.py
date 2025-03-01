# if = Do some code only IF some condition is True
#      Else do something else

"""age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")"""

# Running the code as above:
    # IF input is 18-99 => You are now signed up
    # IF input is -1    => You haven't been born yet
    # IF input is 100+  => You are now signed up (INCORRECT)
                      # => does not take into account the 3rd statement, elif age >= 100:
    # IF input is >18   => You must be 18+ to sign up
# -------------------------------------------------------------------------------------------

# Prompt the user to enter their age and convert the input to an integer
age = int(input("Enter your age: "))

# Check if the age is 100 or older
if age >= 100:
    # Inform the user that they are too old to sign up
    print("You are too old to sign up")

# Check if the age is 18 or older (but less than 100)
elif age >= 18:
    # Inform the user that they are now signed up
    print("You are now signed up")

# Check if the age is negative
elif age < 0:
    # Inform the user that they haven't been born yet
    print("You haven't been born yet")

# If none of the above conditions are met, the age is less than 18 but not negative
else:
    # Inform the user that they must be 18 or older to sign up
    print("You must be 18+ to sign up")

# Running the code as above:
    # IF input is 100+  => You are too old to sign up
    # IF input is 18-99 => You are now signed up
    # IF input is -1    => You haven't been born yet
    # IF input is >18   => You must be 18+ to sign up