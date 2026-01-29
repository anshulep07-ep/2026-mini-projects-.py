import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("========== PASSWORD GENERATOR ==========")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    )

    if password is None:
        print("Error: Please select at least one character type.")
    else:
        print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
