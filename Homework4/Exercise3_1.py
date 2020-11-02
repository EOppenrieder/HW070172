#A program that calculates the volume and surface area
# of a sphere from its radius

pi = 3.141592653589793
def main():
    r = int(input("Please enter the radius in cm: "))
    V = 4 / 3 * pi * (r**3)
    A = 4 * pi * (r**2)
    print("The volume of your sphere is:", V, "cm³")
    print("The surface area of your sphere is:", A, "cm²")

main()