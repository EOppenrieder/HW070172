# A program to calculate Fibonacci numbers

import math

def fibonacci(n):
    x = 0
    y = 1
    z = 0

    for i in range(n-1):
        z = x + y
        x = y
        y = z
    return y

def main():
    n = int(input("Enter the number in the Fibonacci sequence you want to know: "))
    y = fibonacci(n)
    print("The", n, "th Fibonacci number is", y, ".")

main()