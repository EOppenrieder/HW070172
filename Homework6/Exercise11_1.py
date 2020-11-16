#stats.py extended version

from math import sqrt

def getNumbers():
    nums = []
    xStr = input("Enter a number: ")
    while xStr != " ":
        x = float(xStr)
        nums.append(x)
        xStr = input("Enter a number: ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums):
    xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(nums):
    xbar = mean(nums)
    std = stdDev(nums)
    return xbar, std

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos-1]) / 2.0
    else:
        med = nums[midPos]
    return med

def main():
    num = input("Enter a series of numbers, separated by commas: ")
    nums = num.split(",")
    for i in range(len(nums)):
        nums[i] = eval(nums[i])
    x = 0
    while x != " ":
        x = (input("Type 'Avg', 'Med', 'Std' or 'AvgStd': "))
        if x == 'Avg':
            print(mean(nums))
        elif x == 'Med':
            print(median(nums))
        elif x == 'Std':
            print(stdDev(nums))
        elif x == 'AvgStd':
            print(meanStdDev(nums))
        elif x == " ":
            break
        else:
            print("Please try again.")

main()

