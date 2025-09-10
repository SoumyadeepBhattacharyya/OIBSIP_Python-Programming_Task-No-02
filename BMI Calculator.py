def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

while True:
    try:
        weight = float(input("Enter your weight (in KG): "))
        height = float(input("Enter your height (in Meter): "))

        # Validation check
        if weight <= 0 or height <= 0:
            print(" Weight and Height must be positive numbers. Try again.\n")
            continue

        bmi = calculate_bmi(weight, height)
        print(f"\n Your BMI is: {bmi:.2f}")

        # Classification
        if bmi < 18.5:
            print("You are Underweight")
        elif 18.5 <= bmi < 24.9:
            print("You are Normal weight")
        elif 25 <= bmi < 29.9:
            print("You are Overweight")
        else:
            print("You are Obese")
        break  # Exit loop after successful calculation

    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
    except ZeroDivisionError:
        print(" Height cannot be zero. Try again.\n")

