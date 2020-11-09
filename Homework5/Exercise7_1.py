# A program to calculate your wage
def main():
    n = float(input("Enter the number of hours you worked this week: "))
    rate = float(input("Enter your wage per hour: "))
    if n > 40:
        wage = 40*rate + (n-40)*1.5*rate
    else:
        wage = n*rate

    print("Your wage per week is", wage, "dollars.")

main()
