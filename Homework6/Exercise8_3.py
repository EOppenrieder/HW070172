#A program to tell you how long it takes to double your investment
def main():
    init = float(input("Enter your initial investment: "))
    r = float(input("Enter the annual interest rate: "))
    years = 0
    interest = 0
    invest = init
    while init > 0.5*invest:
        interest = invest*r
        invest = invest + interest
        years = years + 1
    print(years)
    print(invest)

main()