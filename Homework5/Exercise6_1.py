#A program to print the lyrics of "Old MacDonald"
def OldMac():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
def verse(animal, sound):
    OldMac()
    print("And on that farm, he had a", animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a", sound + ",", sound + ", here and a", sound + ",", sound + ", there.")
    print("Here a", sound + ", there a", sound + ", everywhere a", sound + ",", sound + ".")
    OldMac()

def main():
    verse("sheep", "meck")
    print()
    verse("goat", "gack")
    print()
    verse("pig", "oink")
    print()
    verse("bird", "tirili")
    print()
    verse("donkey", "iah")

main()

