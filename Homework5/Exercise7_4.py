#A program to show your class standing
def main():
    c = int(input("Enter your credits earned: "))
    if c<7:
        print("You're a Freshman")
    elif 7<=c<16:
        print("You're a Sophomore")
    elif 16<=c<26:
        print("You're a Junior")
    elif c>=26:
        print("Congrats, you are a Senior!")
    else:
        print("Please enter a positive number")

main()