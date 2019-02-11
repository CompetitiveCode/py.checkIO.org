#Answer to Pawn Brotherhood - https://py.checkio.org/en/mission/pawn-brotherhood/

def safe_pawns(pawns: set) -> int:
    pawns = list(pawns) #Changed the set to list
    length = len(pawns) #To get the full length of list
    result = [] #To store the result for each pawn. This is done, so that even if a pawn is saved by two other pawns, still it is counted as 1, meaning safe.
    for i in range(length): #To traverse through all the pawns
        result.append(0) #To add a zero as the default value for all the pawns. 1 denotes safe and 0 denotes unsafe.
    start = 0 #Starting point
    while start < length: #To traverse through all the pawns
        for j in pawns: #To traverse through all the possible saviour of the above pawn
            i=pawns[start] #This is written just for readability. Else we can substitute 'i' for 'pawns[start]' everywhere in this loop
            if ord(i[0]) == ord(j[0])-1: #Checking whether we have any character just less than the character. Ex. for i[0] = c, then j[0] = d
                if int(i[1]) == int(j[1])+1: #Checking whether we have any value just less than the number, denoting the saving pawn to be either left or right of the saved pawn.
                    result[start]=1 #If that pawn is saved by it, then we mark it as 1
            elif ord(i[0]) == ord(j[0])+1: #Checking whether we have any character just greater than the character. Ex. for i[0] = c, then j[0] = b
                if int(i[1]) == int(j[1])+1: #Checking whether we have any value just less than the number, denoting the saving pawn to be either left or right of the saved pawn.
                    result[start]=1 #If that pawn is saved by it, then we mark it as 1
        start+=1 #To check the next value
    return sum(result) #The sum of the values will be the answer.

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")