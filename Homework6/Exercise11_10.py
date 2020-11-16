#A program for the sieve of Erastothenes
def sieve(list):
    newlist = []
    while len(list) != 0:
        newlist.append(list[0])
        try:
            for i in range(len(list)):
                if list[i] % list[0] == 0:
                    list.remove(list[i])
        except:
            newlist
    return newlist

def main():   
    n = int(input("Enter a positive number: "))
    list = []
    for i in range(n-1):
        list.append(i+2)
    list = sieve(list)
    list.remove(4)
    print(list)

main()

