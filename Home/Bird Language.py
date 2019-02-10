#Answer to Bird Language - https://py.checkio.org/en/mission/bird-language/

VOWELS = ['a','e','i','o','u','y']

def translate(phrase):
    length = len(phrase) #To know the length to traverse the string
    start = 0 #The iterating value
    result = "" #To store the result
    while start<length: #Run till the length of the string
        result+=phrase[start] #Adds the character to the result
        if phrase[start] == " ": #If it is just a space, then skip 1 character
            start+=1
        elif  phrase[start] not in VOWELS: #If it is not a vowel, then skip 2 character
            start+=2
        else: #If it is a vowel, then skip 3 character
            start+=3
    return result

if __name__ == '__main__':
    print(translate("hieeelalaooo"))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"