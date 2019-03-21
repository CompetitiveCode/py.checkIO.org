#Answer to Conversion from CamelCase - https://py.checkio.org/en/mission/conversion-from-camelcase/

def from_camel_case(name):
    names = ""
    flag = 0
    for i in name:
        if i.isupper():
            if flag == 0:
                j = i.lower()
                flag = 1
            else:
                j = '_'+i.lower()
        else:
            j = i
        names += j
    return names

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")