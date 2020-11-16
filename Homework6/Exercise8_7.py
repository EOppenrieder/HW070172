#A program for the Goldbach conjecture
import math
def primeNum(n):
    x = math.sqrt(n)
    i = 2
    while i <= x:
        value = n % i 
        if value == 0:
            return None
        else: 
            i = i + 1
    return n

def main():
    x = int(input("Enter a number that is even: "))
    if x % 2 != 0:
        print("Please enter an even number.")
    else:
        n = x
        while n > 0:
            prime = primeNum(n+1)
            if prime != None:
                prime2 = x - prime
                test = primeNum(prime2)
                if test != None:
                    print("{0} + {1} = {2}".format(prime, prime2, x))
            n = n - 1

main()

