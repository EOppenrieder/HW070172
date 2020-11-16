#A program to remove duplicate vaues
def isin(myList, x):
    for i in myList:
        if i == x:
            return True

def removeDuplicates(myList):
    newList = []
    for i in myList:
        if not isin(newList, i):
            newList.append(i)
    return newList

def main():
    myList = [4, 3, 4, 5, 5, 7]
    print(removeDuplicates(myList))

main()