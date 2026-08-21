import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, format_err_msg
# DO NOT CHANGE CODE ABOVE THIS LINE

def calculate_price_percentage(percentage_changes):
    """
    This function is used by a shop to add percentage increases to the price of an item.
    The function will take a list of price increases/decreases as an argument and return the final price as a percentage of the total.

    For example, if a price had a 10% discount from multi-buy and a 15% discount from another offer, then your function would be invoked with a list containing -10 and -15. These would be taken off the original price (100%) returning a final value of 75 (representing 75% of the original).

    Use the built-in sum function to work out the modified percentage.
    https://docs.python.org/3/library/functions.html#sum
    """
    sum_percentage = sum(percentage_changes) * (-1)

    return 100 - sum_percentage


    pass


@run_test
def test_calculate_total():
    assert calculate_price_percentage([-10, -15]) == 75, \
        format_err_msg(75, calculate_price_percentage([-10, -15]))

    assert calculate_price_percentage([20]) == 120, \
        format_err_msg(120, calculate_price_percentage([20]))

    assert calculate_price_percentage([]) == 100, \
        format_err_msg(100, calculate_price_percentage([]))

    assert calculate_price_percentage([-50, 75]) == 125, \
        format_err_msg(125, calculate_price_percentage([-50, 75]))


if __name__ == '__main__':
    test_calculate_total()