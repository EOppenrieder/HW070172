# A program to tell you whether you are eligible for certain positions in the US political system

def main():
    age = float(input("How old are you: "))
    cit = float(input("For how many years have you been an American citizen?: "))
    if age >= 30:
        if cit >= 9:
            print("Congrats, you're eligible to the Senate and the House!")
        elif cit>=7 and cit<9:
            print("You're eligible to the House.")
        elif cit < 7:
            print("Sorry, you're neither eligible to the Senate nor to the House.")
        else:
            print("Please enter positive numbers.")
    elif age <30 and age >= 25:
        if cit >= 7:
            print("You're eligible to the House.")
        elif cit < 7:
            print("Sorry, you're neither eligible to the Senate nor to the House.")
        else:
            print("Please enter positive numbers.")
    elif age < 25:
        print("Sorry, you're neither eligible to the Senate nor to the House.")
    else:
        print("Please enter positive numbers.")

main()
