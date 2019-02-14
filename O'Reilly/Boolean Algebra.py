#Answer to Boolean Algebra - https://py.checkio.org/en/mission/boolean-algebra/

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    value = False
    if operation == OPERATION_NAMES[0]:
        value = x and y
    elif operation == OPERATION_NAMES[1]:
        value = x or y
    elif operation == OPERATION_NAMES[2]:
        value = (not x) or y
    elif operation == OPERATION_NAMES[3]:
        value = (x or y) and (not(x and y))
    elif operation == OPERATION_NAMES[4]:
        value = x == y
    
    if value == True:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"