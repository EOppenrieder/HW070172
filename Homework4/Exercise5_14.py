# A wordcount program

def main():
    fname = input("Enter the name of your file: ")
    infile = open(fname, "r")
    data = infile.read
    numWords = []
    letTotal = 0
    for string in data.split():
        x = string[0]
        numWords.append(x)
    infile.close()

    infile = open(fname, "r")
    fileLines = infile.readlines()

    lines = []
    for line in fileLines:
        lines.append(line)
    print("There are {0} lines in the file.".format(len(lines)))
    print("The total number of letters is {0}".format(letTotal))
    print("The number of words is {0}".format(len(numWords)))
    infile.close()
main()

