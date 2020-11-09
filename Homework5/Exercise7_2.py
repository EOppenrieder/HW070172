#A program to calculate your grade

def main():
    x = int(input("Please enter your quiz score: "))
    if x==5:
        print("A")
    elif x==4:
        print("B")
    elif x==3:
        print("C")
    elif x==2:
        print("D")
    elif x<=1:
        print("F")
    else:
        print("Please enter a number between 0 and 5")

main()
