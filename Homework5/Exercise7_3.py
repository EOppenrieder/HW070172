#Yet another program to calculate your grade
def main():
    x = int(input("Enter your score: "))
    if 90<=x<=100:
        print("A")
    elif 80<=x<90:
        print("B")
    elif 70<=x<80:
        print("C")
    elif 60<=x<70:
        print("D")
    elif x<60:
        print("F")
    else:
        print("Please enter a number between 0 and 100")

main()