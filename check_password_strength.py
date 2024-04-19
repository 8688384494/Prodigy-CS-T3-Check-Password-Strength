import re


def check_password_strength(password):
    length = len(password)
    if length < 8:
        return "Weak: Password length should be at least 8 characters."

    # Check for presence of uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for presence of lowercase letters
    if not re.search("[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for presence of numbers
    if not re.search("[0-9]", password):
        return "Weak: Password should contain at least one number."

    # Check for presence of special characters
    if not re.search("[!@#$%^&*()-+=]", password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all criteria."


def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)


if __name__ == "__main__":
    main()
