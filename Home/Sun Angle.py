#Answer to Sun Angle - https://py.checkio.org/en/mission/sun-angle/

def sun_angle(time):
    text = "I don't see the sun!" #Text to be displayed if the sun is not visible
    result = 0 #To store the angle value
    value = time.split(':') #Splitting the time into two values
    value = int(value[0]+value[1]) #Making that splitted value to a single value
    if (value>1800 and value<2359) or (value>0 and value<600): #Checking the time where the sun won't be visible
        return text
    if (value-600) > 99: #This is done as the value will be from 600-659 then 700-759 and so on.
        result = ((value-600)//100)*15 #Thus we need to extract the 100s value, and that has to be multiplied with 15 (each 100 is 15 degree in angle)
    value %= 100 #This is to extract the minute value from the time, i.e. 0-59
    return result+(value/4) #With the previous 100s value, if any we take the minute's angle. For each 4 minute, we take 1 degree as angle.

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")