#Answer to Speech Module - https://py.checkio.org/en/mission/speechmodule/

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = " hundred"

def checkio(number):
    final = "" #To store the final result
    if number // 100 != 0: #To check the number greater than 99 or not
        final += FIRST_TEN[(number // 100)-1]+HUNDRED #If it is, we need to add the hundred to it
        if number % 100 != 0: #This is to check if it is a perfect hundred
            final += " " #If it is not, then add a space after the text for the other value to be added
    if number % 100 != 0: #To check for number less than hundred
        if number % 100 < 10: #To check if it is below 10
            final += FIRST_TEN[(number % 100) - 1] #Then we can use the FIRST_TEN list
        elif number % 100 > 9 and number % 100 < 20: #If it is between 10 and 19
            final += SECOND_TEN[(number % 100) - 10] #Then we can use the SECOND_TEN list
        else: #If it is a number between 20 and 99
            if number % 10 == 0: #We first have to check if it is a perfect tens value, except 10
                final += OTHER_TENS[((number % 100) // 10) - 2] #If it is, then we use the OTHER_TENS list
            else: #If it has a ones place as well
                final += OTHER_TENS[((number % 100) // 10) - 2] + " " + FIRST_TEN[(number % 10) - 1] #Then we use a combination of both the OTHER_TENS and FIRST_TENS
    return final

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')