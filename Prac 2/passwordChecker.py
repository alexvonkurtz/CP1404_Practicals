"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)

def is_valid_password(password):

    # TODO: if length is wrong, return False
    if len(password) <= 6 and len(password) >= 0:
        return True
    else:
        return False

    # Stuck here due to char checking upper or lower
    for char in password:
        if char.isupper():
            print ("Valid upper")


        # TODO: count each kind of character

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero

    # if we get here (without having returned False), then the password must be valid


main()