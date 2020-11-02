# A batch version of the wordcount-program
def main():
    infilename = input("Enter the name of the infile:" )
    outfilename = input("Enter the name of the outfile: ")
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    data = infile.read()

    numbWords = []
    for string in data.split():
        x = string[0]
        numbWords.append(x)
    
    letTotal = 0
    for string in data.split():
        letTotal = len(string) + letTotal
        wordAvg = letTotal / (len(numbWords))
    print (wordAvg, file=outfile)
    infile.close()
    outfile.close()

main()
