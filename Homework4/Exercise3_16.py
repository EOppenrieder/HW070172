# A program to compute fibonacci numbers


def main():
    n = int(input("Enter the number in the Fibonacci sequence you want to know: "))
    x = 1
    y = 0
    for i in range(n):
        z = x + y
        x = y
        y = z
    print(i+1, ":", y)

main()