#Answer to The Most Wanted Letter - https://py.checkio.org/en/mission/most-wanted-letter/

def checkio(text: str) -> str:
    dictionary = {}
    text = text.lower()
    for i in text:
        if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123):
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    result = sorted(dictionary.items(), key=lambda k: k[1], reverse = True)
    highest = result[0][1]
    result_list = [result[0][0]]
    for i in result:
        if highest == i[1]:
            result_list.append(i[0])
    return sorted(result_list)[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")