# A program to calculate the area of a triangle

import math

def main():
    a = float(input("Enter the length of side a in cm: "))
    b = float(input("Enter the length of side b in cm: "))
    c = float(input("Enter the length of side c in cm: "))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("The area of the triangle is", A, "square cm.")

main()
