# A program to approximate the value of pi
import math

def main():
    n = int(input("Enter the number of terms to sum: "))
    x = 0
    m = 1
    for i in range(1,2*n+1,2):
        x = x + (m*4/i)
        m = -m
    print(x)
    print(abs(math.pi - x))

main()