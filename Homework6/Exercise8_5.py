# A program to determine prime values
import math

def main():
    n = int(input("Please enter a natural number that is bigger than two: "))
    i = 2
    while i <= math.sqrt(n):
            value = n % i
            if value == 0:
                exit()
            else:
                i = i + 1
    print("The number is prime.")
        

main()
