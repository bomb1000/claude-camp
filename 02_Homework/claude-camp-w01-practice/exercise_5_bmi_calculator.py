def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def get_advice(bmi):
    if bmi < 18.5:
        return "Underweight: consider balanced meals and strength training."
    if bmi < 24:
        return "Healthy range: keep your current habits."
    if bmi < 27:
        return "Overweight: add regular exercise and watch portions."
    return "Obese range: consider speaking with a healthcare professional."


def main():
    print("BMI Calculator")
    height_cm = float(input("Enter height in centimeters: "))
    weight_kg = float(input("Enter weight in kilograms: "))
    if height_cm <= 0 or weight_kg <= 0:
        print("Height and weight must be greater than zero.")
        return

    bmi = calculate_bmi(weight_kg, height_cm)
    print(f"Your BMI is {bmi:.1f}")
    print(get_advice(bmi))


if __name__ == "__main__":
    main()
