# Password checker function tested here, itt will be removed probably from here.
def password_checker(sign_up_pw):
    special_chars = ['$', '@', '#', '%', ',', '.', ':', '_', '-', '*', ';', '?']
    is_pw_valid = True

    if len(sign_up_pw) < 6:
        is_pw_valid = False
        print("Too short pw! Please min 6 characters")
    if len(sign_up_pw) > 20:
        is_pw_valid = False
        print("too long pw, max 20 chars")
    if not any(char.isdigit() for char in sign_up_pw):
        is_pw_valid = False
        print("It has to contain min one digit!")
    if not any(char.isupper() for char in sign_up_pw):
        is_pw_valid = False
        print("min one uppercase letter!")
    if not any(char.islower() for char in sign_up_pw):
        is_pw_valid = False
        print("min 1 lowercase please!")
    if not any(char in special_chars for char in sign_up_pw):
        is_pw_valid = False
        print("please min 1 spec. char!")

    return is_pw_valid


def sign_up_email_checker(sign_up_email):
    is_email_valid = True

    if len(sign_up_email) < 8:
        is_email_valid = False

    email_split = sign_up_email.split('@')

    if len(email_split[0]) < 2:
        is_email_valid = False

    return is_email_valid





