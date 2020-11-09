#A program to print the lyrics of "The Ants Go Marching"

def ants():
    number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    verse = ["suck his thumb", "tie his shoe", "stretch his legs", "blow his nose", "hold his hands", "wash his feet", "shout out loud", "make a rhyme", "watch the scene", "think of cheese"]
    for i in range(10):
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(number[i])))
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(number[i])))
        print("The ants go marching {0} by {0},".format(str(number[i])))
        print("The little one stops to {0}".format(str(verse[i]))
        print("And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!")     
def main():
    ants()

main()