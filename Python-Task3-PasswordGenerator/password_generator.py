import random
import string


print("=" * 45)
print("       RANDOM PASSWORD GENERATOR")
print("=" * 45)


while True:

    # Password length
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("❌ Password must be at least 8 characters.")
            continue

    except ValueError:
        print("❌ Please enter a valid number.")
        continue


    # Character type selection
    print("\nChoose character types:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$%^&*)")

    choices = input(
        "\nEnter your choices (example: 1,2,3,4): "
    )

    choices = choices.replace(" ", "").split(",")
    choices = list(set(choices))


    # Check for invalid choices
    valid_choices = {"1", "2", "3", "4"}

    if not set(choices).issubset(valid_choices):
        print("❌ Invalid character type selected.")
        continue


    # At least 2 character types required
    if len(choices) < 2:
        print("❌ Please select at least 2 character types.")
        continue


    # Create character pool
    characters = ""

    if "1" in choices:
        characters += string.ascii_uppercase

    if "2" in choices:
        characters += string.ascii_lowercase

    if "3" in choices:
        characters += string.digits

    if "4" in choices:
        characters += "!@#$%^&*"


    # Generate at least one character from each selected type
    password = ""

    if "1" in choices:
        password += random.choice(string.ascii_uppercase)

    if "2" in choices:
        password += random.choice(string.ascii_lowercase)

    if "3" in choices:
        password += random.choice(string.digits)

    if "4" in choices:
        password += random.choice("!@#$%^&*")


    # Fill remaining characters
    for i in range(length - len(password)):
        password += random.choice(characters)


    # Shuffle password
    password = list(password)
    random.shuffle(password)
    password = "".join(password)


    # Display password
    print("\n" + "-" * 45)
    print("Generated Password:", password)
    print("-" * 45)


    # Ask user whether to generate another password
    while True:
        again = input("\nGenerate another password? (y/n): ").strip().lower()

        if again == "y":
            break

        elif again == "n":
            print("\nThank you for using Password Generator!")
            exit()

        else:
            print("❌ Please enter only 'y' or 'n'.")