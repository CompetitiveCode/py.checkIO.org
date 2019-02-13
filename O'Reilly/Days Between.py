#Answer to Days Between - https://py.checkio.org/en/mission/days-diff/

from datetime import date

def days_diff(date1, date2):
    date1 = date(date1[0],date1[1],date1[2]) #Converting it into date object
    date2 = date(date2[0],date2[1],date2[2])
    d = date2 - date1 #Putting the difference parameter into d
    return abs(d.days) #Taking the difference and producing it as days and also converting it to absolute value

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238