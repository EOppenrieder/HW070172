def main():
    print("This program calculates the total accumulation")
    print("of an investment plan based on annual investment amounts.")

    amount = eval(input("Enter the amount you invest each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the years of investment: "))

    for i in [years]:
        amount = amount * (1 + apr) * years

        print("The accumulative value is: ", amount)

main ()