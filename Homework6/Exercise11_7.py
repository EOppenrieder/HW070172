#A program for the inner function of two lists
def main():
    xList = [4, 7, 10, 3, 6, 2]
    yList = [8, 2, 11, 6, 5, 4]

    total = 0
    for i in range(len(xList)):
        x = xList[i] * yList[i]
        total = total + x
    print(total)

main()
