# A program for the Syracuse sequence

def main():
    x = int(input("Enter a natural number: "))
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            print(x)
        elif x % 2 == 1:
            x = 3*x + 1
            print(x)
        else:
            print("Please enter a natural number.")

main()