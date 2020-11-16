#A censor program
def main():
    filename = eval(input("Enter a filename: "))
    infile = open(filename, "r")
    outfile = open("newfile.txt", "w")
    for line in infile:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) == 4:
                words[i] == "****"
            line = " ".join(words)
            print((line), file = outfile)
        infile.close()
        outfile.close()

main()