# A program to count the number of words in a sentence
def main():
    text = input("Enter your sentence: ")
    word_len = []
    for string in text.split():
        x = string[0]
        word_len.append(x)
    print(len(word_len))

main()