# A program to calculate the cost of a babysitter

def main():
    start = input("Please enter the starting time in hours and minutes, separated by a colon: ")
    end = input("Please enter the ending time in hours and minutes, separated by a colon: ")
    starthour, startmin = start.split(":")
    endhour, endmin = end.split(":")
    sh = int(starthour)
    sm = int(startmin)
    eh = int(endhour)
    em = int(endmin)
    time1 = eh - sh
    time2 = em - sm
    if time2 < 0:
        time2 = abs(time2)
        time1 = time1 - 1
    else:
        time2 = time2
        time1 = time1 
    if eh < 21:
        cost = 2.5 * time1 + (2.5 / 60) * time2
    else:
        x = eh - 21
        cost = 2.5 * (time1 + 1 - x) + (2.5 / 60) * abs(0 - sm) + 1.75 * x + (1.75 / 60) * em
    print(cost)
main()