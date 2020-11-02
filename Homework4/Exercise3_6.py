# A program to calculate the slope of a line
# through two non-vertical points in a plane

def main():
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    slope = (y2-y1) / (x2-x1)
    print(slope)

main()