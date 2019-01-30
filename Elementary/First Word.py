#Answer to First Word - https://py.checkio.org/en/mission/first-word/

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    for i in text.split(' '):
        if i!="" and i.isalpha():
            return i
        else:
            ret_text = ""
            flag = 0
            for j in i:
                if j.isalpha() or j == "'":
                    ret_text += j
                else:
                    if ret_text != "":
                        return ret_text
            if ret_text != "":
                return ret_text

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")