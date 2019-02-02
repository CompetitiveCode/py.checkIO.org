#Answer to Popular Words - https://py.checkio.org/en/mission/popular-words/

import re
def popular_words(text: str, words: list) -> dict:
    dictionary = {}
    for i in words:
        count = sum(1 for _ in re.finditer(r'\b%s\b' %re.escape(i), text, re.I))
        dictionary[i] = count
    return dictionary


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")