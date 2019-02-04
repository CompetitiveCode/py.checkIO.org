#Answer to Absolute Sorting - https://py.checkio.org/en/mission/absolute-sorting/

def checkio(numbers_array: tuple) -> list:
    num_list = []
    for i in numbers_array:
        j = i
        if j < 0:
            j*=-1
        num_list.append(j)
    num_list = sorted(num_list)
    for i in range(len(num_list)):
        if num_list[i]*-1 in numbers_array:
            num_list[i]*=-1
    return num_list

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")