def main ():
    print("This program calculates the future value")
    print("of an investment for a given time period.")

    principal = eval(input("Enter the initial principal: "))
    intrate = eval(input("Enter the interest rate per year: "))
    periods = eval(input("Enter the number of times the interest is compounded in a year: "))
    years = eval(input("Enter the number of years of investment: "))

    for i in range(years):
        principal = principal * ((intrate / periods) * periods + 1)
        print("The value of your investment is:", principal)
    
main ()