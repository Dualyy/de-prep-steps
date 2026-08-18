import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE


# Challenge 0
# This function should return the product of two passed numbers.
def multiply(a,b):
    return a * b
    pass


@run_test
def test_multiply():
    assert multiply(3, 5) == 15, format_err_msg(15, multiply(3, 5))
    assert multiply(17, 19) == 323, format_err_msg(15, multiply(17, 19))
    assert multiply(-180, 2) == -360, format_err_msg(15, multiply(-180, 2))


# Challenge 1
# This function should take a single argument and return its value rounded
# DOWN to the nearest integer.
def round_down(number):
    return int(number)
    pass


@run_test
def test_round_down():
    assert round_down(100.1) == 100, format_err_msg(100, round_down(100.1))
    assert round_down(25.5) == 25, format_err_msg(100, round_down(25.5))
    assert round_down(121.999) == 121, format_err_msg(100, round_down(121.999))


# Challenge 2
# This function should take two arguments, m and n, and return m raised to the
# power of n.
def raise_to_power(number,power_of):
    return number ** power_of
    pass


@run_test
def test_raise_to_power():
    assert raise_to_power(10, 3) == 1000, format_err_msg(1000, raise_to_power(10, 3))
    assert raise_to_power(25, 2) == 625, format_err_msg(625, raise_to_power(25, 2))
    assert raise_to_power(10, 0) == 1, format_err_msg(1, raise_to_power(10, 0))


# Challenge 3
# This function should take a number as an argument
# and return True if it is a multiple of 6, False otherwise.
def is_multiple_of_6(number):
    if number % 6 == 0:
        return True
    else: return False
    pass


@run_test
def test_is_multiple_of_6():
    assert is_multiple_of_6(6) is True, format_err_msg(True, is_multiple_of_6(6))
    assert is_multiple_of_6(10) is False, format_err_msg(False, is_multiple_of_6(10))
    assert is_multiple_of_6(15) is False, format_err_msg(False, is_multiple_of_6(15))
    assert is_multiple_of_6(36) is True, format_err_msg(True, is_multiple_of_6(36))
    assert is_multiple_of_6(60) is True, format_err_msg(True, is_multiple_of_6(60))
    assert is_multiple_of_6(61) is False, format_err_msg(False, is_multiple_of_6(61))


# Challenge 4
# This function should take a string as an argument and return
# the same string with the first letter capitalised.


def capitalise_first_letter(string):
    return string.title() 
    pass


@run_test
def test_capitalise_first_letter():
    assert capitalise_first_letter("bang") == "Bang", format_err_msg(
        "Bang", capitalise_first_letter("bang")
    )
    assert capitalise_first_letter("apple") == "Apple", format_err_msg(
        "Apple", capitalise_first_letter("apple")
    )
    assert capitalise_first_letter("coding") == "Coding", format_err_msg(
        "Coding", capitalise_first_letter("coding")
    )


# Challenge 5
# This function should take a integer as an argument representing a year,
# and return true if that year is in the 20th century and false otherwise.


def is_in_the_20th_century(year):
    if year > 1900 and year <= 2000:
        return True
    else: return False
    pass


@run_test
def test_is_in_the_20th_century():
    assert is_in_the_20th_century(1962) is True, format_err_msg(
        True, is_in_the_20th_century(1962)
    )
    assert is_in_the_20th_century(1901) is True, format_err_msg(
        True, is_in_the_20th_century(1901)
    )
    assert is_in_the_20th_century(1900) is False, format_err_msg(
        False, is_in_the_20th_century(1900)
    )
    assert is_in_the_20th_century(1913) is True, format_err_msg(
        True, is_in_the_20th_century(1913)
    )
    assert is_in_the_20th_century(1876) is False, format_err_msg(
        False, is_in_the_20th_century(1876)
    )
    assert is_in_the_20th_century(2001) is False, format_err_msg(
        False, is_in_the_20th_century(2001)
    )
    assert is_in_the_20th_century(2000) is True, format_err_msg(
        True, is_in_the_20th_century(2000)
    )


# Challenge 6
# This function should take a string as an argument representing a file path
# and return True if it is an absolute path, and False otherwise.
# HINT: all absolute file paths start with a /


def is_absolute_path(path):
    if path.startswith("/"):
        return True
    else: return False
    pass


@run_test
def test_is_absolute_path():
    assert is_absolute_path("/Users/mitch") is True, format_err_msg(
        True, is_absolute_path("/Users/mitch")
    )
    assert (
        is_absolute_path("/Users/mitch/northcoders/remote_course/remote_precourse_1")
        is True
    ), format_err_msg(
        True,
        is_absolute_path("/Users/mitch/northcoders/remote_course/remote_precourse_1"),
    )
    assert is_absolute_path("../composers") is False, format_err_msg(
        False, is_absolute_path("../composers")
    )
    assert (
        is_absolute_path("./applications/my-awesome-app.js") is False
    ), format_err_msg(False, is_absolute_path("./applications/my-awesome-app.js"))


# Challenge 7
# This function should take a string as an argument and return a string
# which describes the ASCII code of that character
# The returned string should be in the following format:
# "The ASCII code for <character> is <character-code>"


def get_char_code(char):
    ascii = ord(char)
    return f'The ASCII code for {char} is {ascii}'
    pass


@run_test
def test_get_char_code():
    assert get_char_code("A") == "The ASCII code for A is 65", format_err_msg(
        "The ASCII code for A is 65", get_char_code("A")
    )
    assert get_char_code("b") == "The ASCII code for b is 98", format_err_msg(
        "The ASCII code for b is 98", get_char_code("b")
    )
    assert get_char_code("z") == "The ASCII code for z is 122", format_err_msg(
        "The ASCII code for z is 122", get_char_code("z")
    )
    assert get_char_code("k") == "The ASCII code for k is 107", format_err_msg(
        "The ASCII code for k is 107", get_char_code("k")
    )
    assert get_char_code("!") == "The ASCII code for ! is 33", format_err_msg(
        "The ASCII code for ! is 33", get_char_code("!")
    )
    assert get_char_code("M") == "The ASCII code for M is 77", format_err_msg(
        "The ASCII code for M is 77", get_char_code("M")
    )


# Challenge 8
# This function should take a length and a character as arguments
# and return a list of the given length populated with the given character.


def create_list(length,char):
    result = []
    for x in range(0,length):
        result.append(char)
    return result
    pass


@run_test
def test_create_list():
    assert create_list(3, "!") == ["!", "!", "!"], format_err_msg(
        ["!", "!", "!"], create_list(3, "!")
    )
    assert create_list(5, "a") == ["a", "a", "a", "a", "a"], format_err_msg(
        ["a", "a", "a", "a", "a"], create_list(5, "a")
    )


# Challenge 9
# This function should take a integer representing a battery level
#  as a percentage.
# If the battery level is less than or equal to 5%, then you should return
#  a string stating:
#     "Warning - battery level low: <number-here>%, please charge your device"
# If the battery level is between 5 and 99% then it should return a
#  string stating:
#     "Battery level: <number-here>%"
# If the battery level is 100% then it should return a string stating:
#     "Fully charged :)"


def check_battery_level(battery_level):

    if battery_level <= 5:
        return f'Warning - battery level low: {battery_level}%, please charge your device'
    elif battery_level >= 5 and battery_level < 100:
        return f'Battery level: {battery_level}%'
    else:
        return "Fully charged :)"
    
    pass


@run_test
def test_check_battery_level():
    assert check_battery_level(100) == "Fully charged :)", format_err_msg(
        "Fully charged :)", check_battery_level(100)
    )

    assert check_battery_level(99) == "Battery level: 99%", format_err_msg(
        "Battery level: 99%", check_battery_level(99)
    )
    assert check_battery_level(80) == "Battery level: 80%", format_err_msg(
        "Battery level: 80%", check_battery_level(80)
    )
    assert check_battery_level(30) == "Battery level: 30%", format_err_msg(
        "Battery level: 30%", check_battery_level(30)
    )
    assert check_battery_level(10) == "Battery level: 10%", format_err_msg(
        "Battery level: 10%", check_battery_level(10)
    )
    assert check_battery_level(6) == "Battery level: 6%", format_err_msg(
        "Battery level: 6%", check_battery_level(6)
    )

    assert (
        check_battery_level(5)
        == "Warning - battery level low: 5%, please charge your device"
    ), format_err_msg(
        "Warning - battery level low: 5%, please charge your device",
        check_battery_level(5),
    )
    assert (
        check_battery_level(4)
        == "Warning - battery level low: 4%, please charge your device"
    ), format_err_msg(
        "Warning - battery level low: 4%, please charge your device",
        check_battery_level(4),
    )
    assert (
        check_battery_level(3)
        == "Warning - battery level low: 3%, please charge your device"
    ), format_err_msg(
        "Warning - battery level low: 3%, please charge your device",
        check_battery_level(3),
    )
    assert (
        check_battery_level(1)
        == "Warning - battery level low: 1%, please charge your device"
    ), format_err_msg(
        "Warning - battery level low: 1%, please charge your device",
        check_battery_level(1),
    )


# Challenge 10
# This function should take a list as an argument and return a list containing
# all string elements from the input (retaining the order)


def collect_strings(input_list):
    strlist = []
    for item in input_list:
        if type(item) == str:
            strlist.append(item)
    return strlist
    pass


@run_test
def test_collect_strings():
    assert collect_strings(["a", "b", "c"]) == ["a", "b", "c"], format_err_msg(
        ["a", "b", "c"], collect_strings(["a", "b", "c"])
    )
    assert collect_strings(["a", 10, "b", 1000, "c"]) == [
        "a",
        "b",
        "c",
    ], format_err_msg(["a", "b", "c"], collect_strings(["a", 10, "b", 1000, "c"]))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":
    test_multiply()
    test_round_down()
    test_raise_to_power()
    test_is_multiple_of_6()
    test_capitalise_first_letter()
    test_is_in_the_20th_century()
    test_is_absolute_path()
    test_get_char_code()
    test_create_list()
    test_check_battery_level()
    test_collect_strings()
