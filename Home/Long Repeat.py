#Answer to Long Repeat - https://py.checkio.org/en/mission/long-repeat/

def long_repeat(line):
    length,start,max_count,count = len(line),0,0,0
    if length>0:
        char = line[0]
    while start<length:
        if char == line[start]:
            count+=1
            if max_count<count:
                max_count=count
        else:
            char = line[start]
            count = 1
        start+=1
    return max_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')