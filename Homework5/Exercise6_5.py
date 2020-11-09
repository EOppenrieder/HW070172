#A program to calculate the cost of your pizza
import math
def Area(d):
    r = d / 2
    area = 4*math.pi*(r**2)
    return area

def pricepersquareinch(p, area):
    ppsq = p / area
    return ppsq

def main():
    d = float(input("Enter the diameter of your pizza in inches: "))
    p = float(input("Enter the price of your pizza in dollars: "))
    A = Area(d)
    ppsq = p / A
    print("The area of your pizza is", A, "and the cost per square inch of your pizza is", ppsq, "dollars")

main()