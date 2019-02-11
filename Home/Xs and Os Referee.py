#Answer to Xs and Os Referee - https://py.checkio.org/en/mission/x-o-referee/

from typing import List

def checkio(game_result: List[str]) -> str:
    start=0 #Used as an iterating variable
    for i in game_result: #To check the horizontal values
        if i[0] == i[1] == i[2] and i[0] != '.': #If the horizontal values are equal
            return i[0] #Then that is the winner
    while start<len(game_result): #To check the vertical values
        if game_result[0][start] == game_result[1][start] == game_result[2][start] and game_result[0][start] != '.':
            return game_result[0][start]
        start+=1
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[1][1] != '.': #To check one diagonal value
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[1][1] != '.': #To check the other diagonal value
        return game_result[0][2]
    return "D" #If no winner was found, then it is a Draw

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")