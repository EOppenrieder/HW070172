# A program to convert quiz scores into grades

def main():
    scale = ["F", "F", "D", "C", "B", "A"]
    n = int(input("Enter your quiz score (0-5): "))
    print("Your grade is", scale[n] + ".")

main()