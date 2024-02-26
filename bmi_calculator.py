def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI)
    Formula: BMI = weight / (height * height), where weight is in kilograms and height is in meters
    """
    bmi = weight / (height ** 2)
    return bmi


def main():
    print("Welcome to the BMI Calculator!")
    print("Please enter your weight (in kilograms) and height (in meters) below:")

    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are in the normal weight range.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")


if __name__ == "__main__":
    main()
