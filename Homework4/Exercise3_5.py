# A program to calculate the cost of an order
# at the Konditorei coffee shop

def main():
    coff = float(input("Enter the amount of coffee you want to order in pounds: "))
    coffcost = 10.50 * coff
    shipcost = 0.86 * coff
    totalcost = coffcost + shipcost + 1.50
    print("Your order costs in total", totalcost, "dollars.")

main()