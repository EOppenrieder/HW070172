#A program to create a shuffle-function
from random import random

def shuffle(myList):
    newList = []
    for i in range(len(myList)):
        x = int(random()*len(myList)) - 1
        newList.append(myList[x])
        myList.remove(myList[x])
    return newList

def main():
    myList = [2, 5, 7, 3, 4, 15]
    myList = myList
    print(shuffle(myList))
main()
