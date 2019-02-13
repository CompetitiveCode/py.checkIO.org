#Answer to Median - https://py.checkio.org/en/mission/median/

from typing import List

def checkio(data: List[int]) -> [int, float]:
    data = sorted(data) #Only sorted one can be checked for median
    length = len(data) #To get the complete length of the list
    middle = length//2 #To get the center of the list
    if length%2 != 0: #If it is an odd number
        return data[middle] #Then the middle value from the list is the median
    else: #If it contains even number of list
        return (data[middle] + data[middle-1])/2 #Then the average value of two of the middle values from the list is the median

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")