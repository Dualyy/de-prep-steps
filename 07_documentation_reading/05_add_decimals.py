import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, format_err_msg
# DO NOT CHANGE CODE ABOVE THIS LINE


def add_decimals(fractions_to_add):
    """
    This function will take a list of decimals represented as strings and return the total of all of them added together. 
    There should be no rounding errors, and the result should be returned as a string.
    
    When storing decimal numbers, we often run into a precision problem with how many numbers we can store in memory. 
    Python, like many other languages, uses floats to represent decimal numbers by default.

    `type(0.1) # <class 'float'>`

    These are very flexible but can lead to some unintuitive and rather famous rounding errors. Because computers use a base 2 system to store data (represented by 1's and 0's), there's a limit to how many digits of a decimal number can be stored in memory. These numbers are rounded to use a sensible amount of memory, but we do lose a small amount of precision. Most of the time this won't matter, but sometimes rounding numbers like this can produce some odd results.

    One of the most famous cases is:   
    `print(0.1 + 0.2) # 0.30000000000000004`

    Python provides a decimal module that doesn't use floats and can be used to perform decimal arithmetic accurately:
    https://docs.python.org/3/library/decimal.html#module-decimal
    """
    from decimal import Decimal

    return sum([Decimal(decimal) for decimal in fractions_to_add]).to_eng_string()
    pass


@run_test
def test_add_decimals():
    assert add_decimals(["0.1", "0.2"]) == "0.3", \
        format_err_msg("0.3", add_decimals(["0.1", "0.2"]))

    assert add_decimals(["0.1", "0.1", "0.1", "0.1"]) == "0.4", \
        format_err_msg("0.4", add_decimals(["0.1", "0.1", "0.1", "0.1"]))


if __name__ == '__main__':
    test_add_decimals()