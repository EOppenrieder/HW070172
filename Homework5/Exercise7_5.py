# A program to tell you whether your weight is appropriate
def main():
    weight = float(input("Please enter your weight in pounds: "))
    height = float(input("Please enter your height in inches: "))
    BMI = (weight * 720) / (height**2)
    if BMI > 25: 
        print("You're above the healthy range")
    elif 19 <= BMI <= 25:
        print("You're in the healthy range")
    elif BMI < 19:
        print("You're below the healthy range")
    else:
        print("Please enter a valid height and weight")

main()
