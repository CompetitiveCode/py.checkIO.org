#Answer to The Angles of a Triangle - https://py.checkio.org/en/mission/triangle-angles/

from typing import List
import math

def checkio(a: int, b: int, c: int) -> List[int]:
    if a+b <= c or b+c <= a or a+c <= b: #Checking whether creation of a triangle is possible
        return [0, 0, 0]
    else:
        d = []
        d.append(round(math.acos((b**2 + c**2 - a**2)/(2*b*c))*180/math.pi)) #This is how the angle is found
        d.append(round(math.acos((a**2 + c**2 - b**2)/(2*a*c))*180/math.pi)) #When three sides are available
        d.append(round(math.acos((a**2 + b**2 - c**2)/(2*a*b))*180/math.pi)) #To determine the inside angles
        return sorted(d) #Sorted array is returned as the ascending order is required in the mission

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")