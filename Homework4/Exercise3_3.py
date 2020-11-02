# A program to calculate the molecular weight
# of a carbohydrate (in grams per mole)

def main():
    H = int(input("Enter the number of hydrogen atoms: "))
    C = int(input("Enter the number of carbon atoms: "))
    O = int(input("Enter the number of oxygen atoms: "))
    Hweight = 1.00794
    Cweight = 12.0107
    Oweight = 15.9994
    molweight = H * Hweight + C * Cweight + O * Oweight
    print("The molecular weight of your carbohydrate is", molweight, "grams per mole.")

main()