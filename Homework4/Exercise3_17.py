# A program to guess the square root of numbers

def main():
    x = float(input("Enter the number of which you want to know the square root: "))
    n = int(input("Enter the number of times to improve the guess: "))
    g = x / 2
    for i in range (n):
        g = (g + x / g) / 2
    print(g)
    import math
    print (g, ":", (math.sqrt(x) - g))

main()
