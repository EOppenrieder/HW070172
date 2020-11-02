# A program to calculate the numeric value of a single name

def main():
    n = input("Enter your name: \n")
    n = n.lower()
    x = 0
    for ch in n:
        x = int(ord(ch)) + x - 96
        print("The numeric value of your name is {0}.".format(x))

main()