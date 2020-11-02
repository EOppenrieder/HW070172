# A program that calculates the cost of your pizza,
# given you eat a circular pizza and can tell its diameter

def main():
    d = float(input("Enter the diameter of your pizza in inches: "))
    price = float(input("Enter the price of your pizza in dollars: "))
    r = d / 2
    pi = 3.141592653589793
    A = 4 * pi * (r**2)
    pricepersquareinch = price / A
    print("The cost per square inch of your pizza is", pricepersquareinch, "dollars")

main()

