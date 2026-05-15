def calculate(left, operator, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator in ("*", "x", "×"):
        return left * right
    if operator in ("/", "÷"):
        if right == 0:
            return "Cannot divide by zero."
        return left / right
    return "Unsupported operator."


def parse_number(prompt):
    value = input(prompt).strip()
    if value.lower() == "quit":
        return None
    try:
        return float(value)
    except ValueError:
        print("Please enter a valid number.")
        return "invalid"


def main():
    print("Safe Calculator")
    print("Type quit at any number prompt to exit.")
    while True:
        left = parse_number("First number: ")
        if left is None:
            print("Goodbye!")
            break
        if left == "invalid":
            continue
        operator = input("Operator (+, -, *, /): ").strip()
        right = parse_number("Second number: ")
        if right is None:
            print("Goodbye!")
            break
        if right == "invalid":
            continue
        print(f"Result: {calculate(left, operator, right)}")


if __name__ == "__main__":
    main()
