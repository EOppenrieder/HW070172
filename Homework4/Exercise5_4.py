# A program to create acronyms
def main():
    n = (input("Enter a phrase: \n"))
    words = []
    for string in n.split():
        x = string[0].upper()
        words.append(x)
    acro = "".join(words)
    print(acro)

main()

