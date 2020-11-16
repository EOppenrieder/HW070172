# A program to determine prime values
import math

def prime(n):
    x = math.sqrt(n)
    i = 2
    while i <= x:
            value = n % i
            if value == 0:
                return
            else:
                i = i + 1
    print(n)

def main():
    x = int(input("Please enter a natural number that is bigger than two: "))
    for n in range(x):
            prime(n+1)

main()