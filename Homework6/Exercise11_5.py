#Algorith for python operations
#a)
def count(myList, x):
    total = 0
    for i in myList:
        if i==x:
            total = total + 1
        return total
#b)
def isin(myList, x):
    for i in myList:
        if i==x:
            return True
#c)
def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i
            break
#d)
def reverse(myList):
    newList = []
    for i in range(len(myList)):
        x = myList[-1*(i+1)]
        newList.append(x)
    return newList
#e)
def sort(myList):
    newList = []
    for i in range(len(myList)):
        x = min(myList)
        newList.append(x)
        myList.remove(x)
    return newList

def main():
    myList = [1, 4, 11, 3, 5, 2]
    x = 3
    print(count(myList, x))
    print(isin(myList, x))
    print(index(myList, x))
    print(reverse(myList))
    print(sort(myList))

main()


