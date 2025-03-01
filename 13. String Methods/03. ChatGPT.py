def is_valid_username(username):
    # Check if the username is no more than 12 characters
    if len(username) > 12:
        return False, "Username must be no more than 12 characters long."

    # Check if the username contains spaces
    if ' ' in username:
        return False, "Username must not contain spaces."

    # Check if the username contains any digits
    if any(char.isdigit() for char in username):
        return False, "Username must not contain digits."

    # If all checks pass
    return True, "Username is valid."


def get_username():
    while True:
        username = input("Enter a username: ")
        valid, message = is_valid_username(username)
        if valid:
            print(message)
            return username
        else:
            print(message)
            print("Please try again.")


# Example usage
username = get_username()
