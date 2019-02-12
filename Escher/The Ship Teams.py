#Answer to The Ship Teams - https://py.checkio.org/en/mission/the-ship-teams/

def two_teams(sailors):
    result = [] #To store the result
    temp = [[],[]] #To store the intermediatary values
    for i in sailors.items(): #To get the values of dictionary as Tuple
        if i[1] > 40 or i[1] < 20: #To get the people to be added to the First Ship
            temp[0].append(i[0]) #Adding each person name to first Temp List
        else: #To get the people to be added to the Second Ship
            temp[1].append(i[0]) #Adding each person name to second Temp List
    result.append(sorted(temp[0])) #Adding all the names of the Ship 1 to resultant
    result.append(sorted(temp[1])) #Adding all the names of the Ship 2 to resultant
    return result #Return the result

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))
    print(two_teams({'Fernandes': 18, 'Johnson': 22, 'Kale': 41, 'McCortney': 54}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'], 
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'], 
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")