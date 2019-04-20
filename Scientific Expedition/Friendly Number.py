# Answer to Friendly Number
# https://py.checkio.org/en/mission/friendly-number/


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    sign = ''  # This is when the number would be negative
    if number < 0:  # If the number is negative
        sign = '-'  # Then we assign the negative sign for it
        number = abs(number)  # But we cannot do the operation on the negative number, so we use the absolute for that
    i, check = 0, base  # i is to assign the power and check is just a temp value to see how many times the base is present
    while check > base-1 and i < len(powers):  # First comparison is to see if any more division can be done of not
        check = number // (base ** i)  # Second comparison is to be in the limit of the powers provided by default or through user input
        i += 1  # Each time it is divisible, we add another power to it
    power = i - 1  # As there would be a extra addition to power if the initial case is right, we have to subtract one from it
    number = number / (base ** power)  # Now we need to find the number which is to be displayed
    if not decimals:  # If there is no decimal places, then we need to get the int value of it, without any decimal
        number = int(number)
    return '{0}{1:.{2}f}{3}{4}'.format(sign, number, decimals, powers[power], suffix)

# These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
