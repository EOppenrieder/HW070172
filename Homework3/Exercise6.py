def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the years of investment: "))

    for i in [years]:
        principal = principal * ((1 + apr) ** years)

    print("The value in",years,"years is", principal)

main ()