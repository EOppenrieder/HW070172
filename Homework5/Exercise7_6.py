#A program for the ticket fine policy in Podunksville
def main():
    limit = int(input("Enter the speed limit: "))
    speed = float(input("Enter the speed: "))
    if speed <= limit:
        print("Your speed was legal.")
    else:
        if speed > 90:
            penalty = 50 + 5*(speed-limit) + 200
        else:
            penalty = 50 + 5*(speed-limit)
        print("Your fine amounts to", penalty, "dollars.")

main()
