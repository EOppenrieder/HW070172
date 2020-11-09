# A program to compute the date of Easter
def main():
    year = int(input("Enter a year between 1982 and 2048: "))
    if year > 1981 and year < 2049:
        a = year%19
        b = year%4
        c = year%7
        d = (19*a + 24)%30
        e = (2*b + 4*c + 6*d + 5)%7
        Easter = 22 + d + e
        if Easter > 31:
            print("In", year, ", Easter is on the", Easter - 31, "April.")
        else:
            print("In", year, ", Easter is on the", Easter, "March.")
    else:
        print("Please enter a year between 1982 and 2049.")
main()