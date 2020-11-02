# A program to determine the length of a ladder

import math

pi = 3.141592653589793

def main():
    height = float(input("Enter the height the ladder needs to reach in cm: "))
    angled = float(input("Enter the angle of the ladder in degrees: "))
    angler = pi / 180 * angled
    length = height / math.sin(angler)
    print("The required length of your ladder is", length, "cm.")

main()