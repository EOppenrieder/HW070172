#A program to compute fibonacci numbers
def main():
    x = 0
    y = 1
    z = 1
    n = int(input("Enter the fibonacci number you would like to see: "))
    for i in range(n-2):
        x = y
        y = z
        z = x + y
    print("The", n, "th fibonacci number is", z)

main()
