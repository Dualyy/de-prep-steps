import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE


# If we list all the whole numbers below 10 that are multiples of 3 or 5, we
#  get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3
#  or 5 below the limit passed in as an argument.
# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once!


def find_total_of_multiples(limit):
    sum = 0
    for x in range(0,limit):
        if x % 3 == 0 and x % 5 != 0:
            sum += x
        elif x % 5 == 0 and x % 3 != 0:
            sum += x
        if x % 3 == 0 and x % 5 == 0:
            sum += x
    return sum
    pass


@run_test
def test_find_total_of_multiples():
    # find_total_of_multiples() return zero for negative numbers
    assert find_total_of_multiples(-1) == 0, format_err_msg(
        0, find_total_of_multiples(-1)
    )

    # find_total_of_multiples() returns first multiple of 3
    assert find_total_of_multiples(4) == 3, format_err_msg(
        3, find_total_of_multiples(4)
    )

    # find_total_of_multiples() returns sum of multiples of 3 or 5  below limit

    assert find_total_of_multiples(6) == 8, format_err_msg(
        8, find_total_of_multiples(6)
    )
    assert find_total_of_multiples(10) == 23, format_err_msg(
        23, find_total_of_multiples(10)
    )


# ---------------------------------------------------------------------------

# In a factory a printer prints labels for boxes. For one kind of boxes the
#  printer has to use colors which are named with letters from a to m.
# The colours used by the printer are recorded in a string.

# For example a "good" control string would be aaabbbbhaijjjm meaning that
#  the printer used:
# - colour 'a' three times
# - colour 'b' four times
# - colour 'h' one time
# and so on.

# Sometimes there are problems and a "bad" control string is produced
#  e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# Write a function named count_printer_errors which given a string will
#  return the error rate of the printer.

# You should return a string representing a fraction whose numerator is the
#  number of errors and the denominator the length of the control string.

# Example:
# control = "aaabbbbhaijjjm"
# count_printer_errors(control) should return "0/14"

# control = "aaaxbbbbyyhwawiwjjjwwm"
# count_printer_errors(control) should return "8/22"


def count_printer_errors(error_string):
    COLORS = "abcdefghijklm"
    num_of_errors = 0
    control_string = []
    control_string.extend(error_string)

    for color in control_string:
        if color not in COLORS:
            num_of_errors += 1

    return f'{num_of_errors}/{len(error_string)}'

    pass


@run_test
def test_count_printer_errors():
    # countPrinterErrors() should return zero for an empty control string
    assert count_printer_errors("") == "0/0", format_err_msg(
        "0/0", count_printer_errors("")
    )

    # count_printer_errors() should return correct control string length
    assert count_printer_errors("aaa") == "0/3", format_err_msg(
        "0/3", count_printer_errors("aaa")
    )

    # count_printer_errors() should correctly count errors in control string
    assert count_printer_errors("aaz") == "1/3", format_err_msg(
        "1/3", count_printer_errors("aaz")
    )
    assert count_printer_errors("aaaxbbbbyyhwawiwjjjwwm") == "8/22", format_err_msg(
        "8/22", count_printer_errors("aaaxbbbbyyhwawiwjjjwwm")
    )


# ---------------------------------------------------------------------------
# Ordinal suffixes are the letters we put after a number:
# E.g. "nd" is an ordinal suffix as we'd write 2nd and "st" is an ordinal
#  suffix as we'd write 1st etc

# This function should take a number as an argument and should return the
#  corresponding ordinal suffix

# See here for more details:
#  https://www.grammarly.com/blog/how-to-write-ordinal-numbers-correctly/


def get_ordinal_suffix(num):
    SPECIAL_CASES=["11","12","13"]
    if str(num).endswith('1') and str(num) not in SPECIAL_CASES:
        return 'st'
    elif str(num).endswith('2'):
        return 'nd'
    elif str(num).endswith('3'):
        return 'rd'
    elif str(num) in SPECIAL_CASES:
        return 'th'
    else:
        return 'th'
    pass


@run_test
def test_get_ordinal_suffix():
    # get_ordinal_suffix() returns 'st' when given 1
    assert get_ordinal_suffix(1) == "st", format_err_msg("st", get_ordinal_suffix(1))

    # get_ordinal_suffix() returns 'nd' when given 2
    assert get_ordinal_suffix(2) == "nd", format_err_msg("nd", get_ordinal_suffix(2))

    # get_ordinal_suffix() returns 'rd' when given 3
    assert get_ordinal_suffix(3) == "rd", format_err_msg("rd", get_ordinal_suffix(3))

    # get_ordinal_suffix() returns 'th' given any single digit number above 3
    assert get_ordinal_suffix(4) == "th", format_err_msg("th", get_ordinal_suffix(4))
    assert get_ordinal_suffix(7) == "th", format_err_msg("th", get_ordinal_suffix(7))
    assert get_ordinal_suffix(9) == "th", format_err_msg("th", get_ordinal_suffix(9))

    # get_ordinal_suffix() returns 'th' given any value between 10 and 20
    # inclusive
    assert get_ordinal_suffix(10) == "th", format_err_msg("th", get_ordinal_suffix(10))
    assert get_ordinal_suffix(11) == "th", format_err_msg("th", get_ordinal_suffix(11))
    assert get_ordinal_suffix(15) == "th", format_err_msg("th", get_ordinal_suffix(15))
    assert get_ordinal_suffix(19) == "th", format_err_msg("th", get_ordinal_suffix(19))
    assert get_ordinal_suffix(20) == "th", format_err_msg("th", get_ordinal_suffix(20))

    # get_ordinal_suffix() returns 'st' for numbers above 20 ending in 1
    assert get_ordinal_suffix(21) == "st", format_err_msg("st", get_ordinal_suffix(21))
    assert get_ordinal_suffix(41) == "st", format_err_msg("st", get_ordinal_suffix(41))

    # get_ordinal_suffix() returns 'nd' for numbers above 20 ending in 2
    assert get_ordinal_suffix(22) == "nd", format_err_msg("nd", get_ordinal_suffix(22))
    assert get_ordinal_suffix(32) == "nd", format_err_msg("nd", get_ordinal_suffix(32))

    # get_ordinal_suffix() returns 'rd' for numbers above 20 ending in 3
    assert get_ordinal_suffix(23) == "rd", format_err_msg("rd", get_ordinal_suffix(23))
    assert get_ordinal_suffix(63) == "rd", format_err_msg("rd", get_ordinal_suffix(63))

    # get_ordinal_suffix() returns 'th' for any other numbers
    assert get_ordinal_suffix(27) == "th", format_err_msg("th", get_ordinal_suffix(27))
    assert get_ordinal_suffix(98) == "th", format_err_msg("th", get_ordinal_suffix(98))


# ---------------------------------------------------------------------------


# This function should take a string as its argument and
# return True if each character appears only once and False otherwise
def contains_no_repeats(input):
    input_as_list = list(input)
    if input == "" or input == " ":
        return True
    for char in input_as_list:
        if input_as_list.count(char) > 1:
            return False
    
    return True
    pass


@run_test
def test_contains_no_repeats():
    # contains_no_repeats() returns True for an empty string
    assert contains_no_repeats("") is True, format_err_msg(True, "")

    # contains_no_repeats() returns False for a single repeated character
    assert contains_no_repeats("oo") is False, format_err_msg(False, "oo")
    assert contains_no_repeats("zzz") is False, format_err_msg(False, "zzz")

    # contains_no_repeats() returns True when each character appears only once
    assert contains_no_repeats("dog") is True, format_err_msg(True, "dog")
    assert contains_no_repeats("cat") is True, format_err_msg(True, "cat")
    assert contains_no_repeats("abcde") is True, format_err_msg(True, "abcde")

    # contains_no_repeats() returns False if any characters are repeated
    assert contains_no_repeats("dooog") is False, format_err_msg(False, "dooog")
    assert contains_no_repeats("iHaveRepeats") is False, format_err_msg(
        False, "iHaveRepeats"
    )
    assert contains_no_repeats("anat") is False, format_err_msg(False, "anat")
    assert contains_no_repeats("abcdea") is False, format_err_msg(False, "abcdea")


# ---------------------------------------------------------------------------

# When users are signing up for our service we ask them pick a username.
# Each person's username must be unique and we will write a function to check
#  if their usernames have already been taken or not

# This function should take a list of existing usernames and any number of
#  additional usernames to check
# It should return True if all the new usernames are available, and False if
#  any of them already exist


def check_usernames_available(usernames, *names):
    list_of_names = [*names]
    for name in usernames:
        if name in list_of_names:
            return False
    return True
    pass


@run_test
def test_check_usernames_available():
    # check_usernames_available returns True for a single available username
    assert check_usernames_available(["Roy", "Moss"], "Jen") is True, format_err_msg(
        True, check_usernames_available(["Roy", "Moss"], "Jen")
    )

    # check_usernames_available returns False for a single username that
    #  is taken
    assert check_usernames_available(["Roy", "Moss"], "Moss") is False, format_err_msg(
        False, check_usernames_available(["Roy", "Moss"], "Moss")
    )

    # check_usernames_available returns True for multiple usernames that
    #  are available
    assert (
        check_usernames_available(["Roy", "Moss"], "Jen", "Douglas") is True
    ), format_err_msg(
        True, check_usernames_available(["Roy", "Moss"], "Jen", "Douglas")
    )

    # check_usernames_available returns False for multiple usernames that
    #  are available
    assert (
        check_usernames_available(["Roy", "Moss"], "Roy", "Moss") is False
    ), format_err_msg(False, check_usernames_available(["Roy", "Moss"], "Roy", "Moss"))

    # check_usernames_available returns False if a single username is
    #  not available
    assert (
        check_usernames_available(["Roy", "Moss"], "Jen", "Moss") is False
    ), format_err_msg(False, check_usernames_available(["Roy", "Moss"], "Jen", "Moss"))

    # check_usernames_available returns True if no new usernames are passed
    assert check_usernames_available(["Roy", "Moss"]) is True, format_err_msg(
        True, check_usernames_available(["Roy", "Moss"])
    )


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":
    test_find_total_of_multiples()
    test_count_printer_errors()
    test_get_ordinal_suffix()
    test_contains_no_repeats()
    test_check_usernames_available()
