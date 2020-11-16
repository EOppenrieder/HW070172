# A program to find the Greatest common divisor
def main():
    m = float(input("Please enter a value: "))
    n = float(input("Please enter another value: "))
    while m > 0:
        y = m
        m = n % m
        n = y
    print(n)

main()