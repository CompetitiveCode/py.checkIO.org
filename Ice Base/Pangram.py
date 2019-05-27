# Answer to Pangram
# https://py.checkio.org/en/mission/pangram/


def check_pangram(text):
    text = text.upper() # Convert the string to upper case for ease of checking
    for i in range(ord('A'),ord('Z')+1): # Characters from A to Z
        if chr(i) not in text.upper(): # Check if those characters are present in the provided text
            return False # If not present, immediately return False
    return True # If all the check is complete, that means all the alphabets are present

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
