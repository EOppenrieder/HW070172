# A program that determines the distance to a lightning strike
# based on the time elapsed between the flash and the sound of thunder

def main(): 
    t = int(input("Enter the time elapsed between the moment you saw the flash and the moment you heard the thunder in seconds: "))
    distanceft = t * 1100 
    distancemile = distanceft / 5280
    print("The lightning strike is", distancemile, "miles away.")

main()