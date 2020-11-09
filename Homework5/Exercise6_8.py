# A program to guess the square root of numbers

import math

def nextGuess(guess, x):
    g = (guess + x / guess) / 2
    return g

def main():
    x = float(input("Enter the number of which you want to know the square root: "))
    n = int(input("Enter the number of times to improve the guess: "))
    g = x / 2
    for i in range(n):
        g = nextGuess (g,x)
        print(g)
main()