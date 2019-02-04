#Answer to Even The Last - https://py.checkio.org/en/mission/even-last/

def checkio(array):
    j=0
    if array == []:
        return j
    else:
        j = sum(array[i] for i in range(0,len(array),2))
        return j*array[-1]
            

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")