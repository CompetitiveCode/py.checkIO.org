#Answer to Non-unique Elements - https://py.checkio.org/en/mission/non-unique-elements/

def checkio(data: list) -> list:
    dictionary = {}
    for i in data:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    for i in dictionary:
        if dictionary[i] == 1:
            data.remove(i)
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")