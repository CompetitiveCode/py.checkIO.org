#Answer to Three Words - https://py.checkio.org/en/mission/three-words/

def checkio(words: str) -> bool:
    word_list = words.split()
    three = 0
    for i in word_list:
        if i.isalpha():
            three += 1
        else:
            three = 0
        if three == 3:
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")