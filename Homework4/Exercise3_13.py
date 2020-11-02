# A program to sum a series of numbers

def main():
    n = int(input("Enter the amount of numbers that are to be summed: "))
    x = float(input("Enter a number: "))
    for factor in range(2, n+1):
        y = float(input("Enter a number: "))
        x = x + y
    print(x)
main()