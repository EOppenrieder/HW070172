# A program to calculate the Gregorian epact

def main():
    year = int(input("Enter the year as a 4-digit number: "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8*C + 13)// 25)+ 11*(year % 19)) % 30
    print(epact)

main()