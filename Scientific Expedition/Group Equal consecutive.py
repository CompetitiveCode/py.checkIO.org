# Answer to Group Equal consecutive
# https://py.checkio.org/en/mission/group-equal-consecutive/


def group_equal(els):
    if len(els) == 0:
        return els
    else:
        t1, t2, temp = [], [], els[0]
        for i in els:
            if temp == i:
                t2.append(i)
            else:
                t1.append(t2)
                t2 = [i]
                temp = i
        return t1+[t2]


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
