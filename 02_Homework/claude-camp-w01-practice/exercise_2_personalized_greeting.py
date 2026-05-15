def build_greeting(name, age):
    next_year_age = age + 1
    return (
        f"Hello, {name}! You are {age} years old.\n"
        f"Next year, you will be {next_year_age}.\n"
        "Keep learning and building something useful every week!"
    )


def main():
    print("Personalized Greeting")
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))

    if not name:
        print("Please enter a valid name.")
        return

    print(build_greeting(name, age))


if __name__ == "__main__":
    main()
