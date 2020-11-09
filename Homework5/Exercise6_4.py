#A program to add the sum of natural numbers

def sumN(n):
    fact = 1
    for firstsum in range(n,1,-1):
        fact = fact + firstsum
    return fact

def sumNcubes(n):
    sumc = 1
    for factor in range(2,n+1):
        sumc = sumc + factor ** 3
    return sumc

def main():
    n = int(input("Enter a whole number: "))
    summa = sumN(n)
    cuba = sumNcubes(n)
    print("The sum of the natural numbers is", summa, "and the cube of the natural numbers is", cuba, ".")
    
main()