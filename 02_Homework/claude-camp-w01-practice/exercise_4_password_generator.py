import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def main():
    print("Simple Password Generator")
    length = int(input("Enter password length: "))

    if length < 4:
        print("Please choose a length of at least 4.")
        return

    password = generate_password(length)
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
