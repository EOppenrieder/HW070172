# An improved chaos program

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print("       %.6f     %.6f" % (x,y))
    
main()