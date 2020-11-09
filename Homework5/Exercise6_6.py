#A function to compute the area of a triangle

import math
def area (a,b,c):
    s = (a + b + c) / 2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return A

def main():
    a = float(input("Enter the length of side a in cm: "))
    b = float(input("Enter the length of side b in cm: "))
    c = float(input("Enter the length of side c in cm: "))
    A = area(a,b,c)
    print("The area of the triangle is", A, ".")

main()