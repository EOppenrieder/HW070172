# A program that allows for the calculation of a complete name

def main():
    name = input("Enter your full name: ")
    fullName = "".join(name)
    fullName = fullName.lower()
    fullName = fullName.lstrip()
    x = 0
    for ch in fullName:
        x = int(ord(ch)) + x - 96
    print("The numeric value of your name is {0}.".format(x))

main()