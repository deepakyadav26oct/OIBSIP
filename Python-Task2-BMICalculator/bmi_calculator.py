def show_header():
    print("\n" + "=" * 45)
    print("           BMI CALCULATOR")
    print("=" * 45)
    print("        Python Programming Internship")
    print("             Oasis Infobyte")
    print("=" * 45)


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    show_header()

    while True:
        print("\nEnter your details")
        print("-" * 30)

        try:
            weight = float(input("Weight (kg): "))
            height = float(input("Height (m): "))

            if weight <= 0 or height <= 0:
                print("\n[ERROR] Weight and height must be positive.")
                continue

            bmi = calculate_bmi(weight, height)
            category = get_category(bmi)

            print("\n" + "=" * 45)
            print("              BMI RESULT")
            print("=" * 45)
            print(f"  Weight   : {weight:.2f} kg")
            print(f"  Height   : {height:.2f} m")
            print(f"  BMI      : {bmi:.2f}")
            print(f"  Category : {category}")
            print("=" * 45)

            choice = input("\nCalculate BMI for another person? (Y/N): ")

            if choice.lower() == "n":
                print("\nThank you for using BMI Calculator!")
                print("Have a healthy day! 😊")
                print("=" * 45)
                break

            elif choice.lower() != "y":
                print("[INFO] Please enter Y or N.")

        except ValueError:
            print("\n[ERROR] Please enter numbers only.")


if __name__ == "__main__":
    main()