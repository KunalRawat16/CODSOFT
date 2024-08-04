import random
import string

def generate_password(length):
    """
    Generate a random password of a specified length.
    The password includes a combination of uppercase letters, lowercase letters, digits, and punctuation.

    :param length: The desired length of the password.
    :return: A randomly generated password as a string.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters for better security.")

    # Define character pools for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure at least one character from each category is present
    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random choices from all categories
    all_characters = uppercase + lowercase + digits + punctuation
    password_chars += random.choices(all_characters, k=length - 4)

    # Shuffle the list to prevent predictable patterns
    random.shuffle(password_chars)

    # Join the list into a single string to form the final password
    return ''.join(password_chars)

def main():
    """Main function to run the password generator application."""
    print("Password Generator Application")

    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired length of the password: "))

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated Password: {password}")

    except ValueError as e:
        # Handle invalid inputs and other value errors
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
