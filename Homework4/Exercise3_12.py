# A program to find the sum of cubes of natural numbers

def main():
    n = int(input("Enter a natural number: "))
    sumc = 1
    for factor in range(2,n+1):
        sumc = sumc + factor ** 3
    print(sumc)

main()