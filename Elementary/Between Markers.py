#Answer to Between Markers - https://py.checkio.org/en/mission/between-markers/

def between_markers(text: str, begin: str, end: str) -> str:
    text_1 = ""
    if begin in text:
        text_1 = text.split(begin,1)[1]
        if end in text_1:
            text_1 = text_1.split(end,1)[0]
        elif end in text:
            text_1 = ""
    else:
        text_1 = text.split(end,1)[0]
    return text_1

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')