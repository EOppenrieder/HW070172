# A program to find the average of a series of numbers

def main():
    n = int(input("Enter the amount of numbers you want to be found the average of: "))
    x = float(input("Enter a number: "))
    for factor in range(2,n+1):
        y = float(input("Enter a number: "))
        x = x+y
        average = x / n
    print(average)

main()
