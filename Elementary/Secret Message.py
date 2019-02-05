#Answer to Secret Message - https://py.checkio.org/en/mission/secret-message/

def find_message(text: str) -> str:
    result = ""
    for i in text:
        if ord(i)>64 and ord(i)<91:
            result += i
    return result

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")