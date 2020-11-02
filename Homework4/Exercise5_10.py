# A program to calculate the average
# word length in a sentence

def main():
    text = input("Enter your sentence: ")
    numbWords = []
    for string in text.split():
        x = string[0]
        numbWords.append(x)
    letTotal = 0
    for string in text.split():
        letTotal = len(string) + letTotal
        wordAvg = letTotal / (len(numbWords))
    print(wordAvg)

main()
