#Answer to Conversion into CamelCase - https://py.checkio.org/en/mission/conversion-into-camelcase/

def to_camel_case(name):
    name = name.split("_")
    for i in range(len(name)):
        name[i] = name[i].title()
    return ("").join(name)

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")