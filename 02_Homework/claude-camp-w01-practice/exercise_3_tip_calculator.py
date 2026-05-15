def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * tip_percent / 100
    total = bill_amount + tip
    return tip, total


def main():
    print("Tip Calculator")
    bill_amount = float(input("Enter bill amount: "))
    tip_percent = float(input("Enter tip percentage: "))

    if bill_amount < 0 or tip_percent < 0:
        print("Bill amount and tip percentage must be positive.")
        return

    tip, total = calculate_tip(bill_amount, tip_percent)
    print(f"Bill amount: ${bill_amount:.2f}")
    print(f"Tip ({tip_percent:.1f}%): ${tip:.2f}")
    print(f"Total amount: ${total:.2f}")


if __name__ == "__main__":
    main()
