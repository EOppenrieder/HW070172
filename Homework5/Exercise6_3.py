# Functions for the volume and area of the surface of a sphere
import math
def sphereArea(r):
   area = 4*math.pi*r**2
   return area

def sphereVolume(r):
    Volume = 4/3*math.pi*r**3
    return Volume

def main():
    r = float(input("Enter the radius: "))
    print("The area of a sphere with the radius", r, "is", sphereArea(r), ", and the volume is", sphereVolume(r), ".")

main()