import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

"""
Write a function that takes a string as an argument and returns a boolean
based on whether the word given string ends with 'ing'

check_word_ends_with_ing('hello') returns False
check_word_ends_with_ing('dancing') returns True

"""


def check_word_ends_with_ing(word):

    if word.endswith("ing"):
        return True
    return False

    pass


@run_test
def test_check_word_ends_with_ing():
    assert check_word_ends_with_ing("doing") is True, format_err_msg(
        True, check_word_ends_with_ing("doing")
    )
    assert check_word_ends_with_ing("eating") is True, format_err_msg(
        True, check_word_ends_with_ing("eating")
    )
    assert check_word_ends_with_ing("cry") is False, format_err_msg(
        False, check_word_ends_with_ing("cry")
    )
    assert check_word_ends_with_ing("coder") is False, format_err_msg(
        False, check_word_ends_with_ing("coder")
    )


"""
Write a function that takes a two arguments a and b, and returns the remainder
of a / b

get_remainder(10, 2) returns 0
get_remainder(10, 3) returns 1

"""


def get_remainder(number,divisor):

    return number % divisor

    pass


@run_test
def test_get_remainder():
    assert get_remainder(10, 2) == 0, format_err_msg(0, get_remainder(10, 2))
    assert get_remainder(119, 10) == 9, format_err_msg(
        9, get_remainder(119, 10)
    )
    assert get_remainder(50, 6) == 2, format_err_msg(2, get_remainder(50, 6))


"""
Write a function that takes a dictionary and a key as its arguments and
returns the value found at the provided key in the input dictionary
If the key doesn't exist on the dictionary, this function should return a
string of "property not found"

access_object({"name": "nara", "age": 5}, "name") returns "nara"
access_object({"name": "nara", "age": 5}, "email") returns "property not found"

"""


def access_object(obj, key):

    if key in obj.keys():
        return obj[key]
    else: return  "property not found"

    pass


@run_test
def test_access_object():
    assert (
        access_object({"name": "nara", "age": 5}, "name") == "nara"
    ), format_err_msg(
        "nara", access_object({"name": "nara", "age": 5}, "name")
    )
    assert (
        access_object({"name": "nara", "age": 5}, "age") == 5
    ), format_err_msg(5, access_object({"name": "nara", "age": 5}, "age"))
    assert (
        access_object({"name": "nara", "age": 5}, "email")
        == "property not found"
    ), format_err_msg(
        "property not found",
        access_object({"name": "nara", "age": 5}, "email"),
    )


"""
Write a function that takes a list of numbers as an argument and returns a
list containing all positive numbers from the input (retaining the order)

get_positive_numbers([1, 2, 3]) returns [1, 2, 3]
get_positive_numbers([-1, 2, -3]) returns [2]

"""


def get_positive_numbers(num_list):

    return [num for num in num_list if num > 0]

    pass


@run_test
def test_get_positive_numbers():
    assert get_positive_numbers([1, -1, 2, -2, 3, -3]) == [
        1,
        2,
        3,
    ], format_err_msg([1, 2, 3], get_positive_numbers([1, -1, 2, -2, 3, -3]))
    assert get_positive_numbers([-80, 9, 100, 13, 20, -7]) == [
        9,
        100,
        13,
        20,
    ], format_err_msg(
        [9, 100, 13, 20], get_positive_numbers([-80, 9, 100, 13, 20, -7])
    )
    assert get_positive_numbers([-1, -50, -999]) == [], format_err_msg(
        [], get_positive_numbers([-1, -50, -999])
    )


"""
Write a function that takes a string as its argument and returns a
string consisting of all vowels found in the input (retaining the order)

collect_the_vowels("a) returns "a"
collect_the_vowels("hello") returns "eo"

"""


def collect_the_vowels(sample_string):
    vowels = "aeiou"
    result = ""
    input_list = list(sample_string)
    for char in input_list:
        if char in vowels:
            result += char

    return result

    pass


@run_test
def test_collect_the_vowels():
    assert collect_the_vowels("a") == "a", format_err_msg(
        "a", collect_the_vowels("a")
    )
    assert collect_the_vowels("bcd") == "", format_err_msg(
        "", collect_the_vowels("bcd")
    )
    assert collect_the_vowels("bcdepiaouk") == "eiaou", format_err_msg(
        "eiaou", collect_the_vowels("bcdepiaouk")
    )


"""
Write a function that takes take two arguments, a list and an index, and return
the element at that specified index

The index provided may be equal to or greater than the length of the
given list. In this case, rather than counting past the end of the
list where there are no values, the indexing should be considered to
"loop back around" and continue from the start of the list

access_item(["a", "b", "c", "d"], 2) returns "c"
access_item(["a", "b", "c", "d"], 5) == "b"

"""


def access_item(sample_list, index):
    test_number = index
    if index < len(sample_list) -1:
        return sample_list[index] 
    else:
        return sample_list[index % len(sample_list)]
    pass


@run_test
def test_access_item_retrieves_item_when_passed_index_less_than_list_len():
    assert access_item(["a", "b", "c", "d"], 2) == "c", format_err_msg(
        "c", access_item(["a", "b", "c", "d"], 2)
    )
    assert access_item(["a", "b", "c", "d"], 0) == "a", format_err_msg(
        "a", access_item(["a", "b", "c", "d"], 0)
    )
    assert access_item(["a", "b", "c", "d"], 3) == "d", format_err_msg(
        "d", access_item(["a", "b", "c", "d"], 3)
    )


@run_test
def test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len():
    assert access_item(["a", "b", "c", "d"], 4) == "a", format_err_msg(
        "a", access_item(["a", "b", "c", "d"], 4)
    )
    assert access_item(["a", "b", "c", "d"], 6) == "c", format_err_msg(
        "c", access_item(["a", "b", "c", "d"], 6)
    )
    assert access_item(["a", "b", "c", "d"], 10) == "c", format_err_msg(
        "c", access_item(["a", "b", "c", "d"], 10)
    )


if __name__ == "__main__":
    test_check_word_ends_with_ing()
    test_get_remainder()
    test_access_object()
    test_collect_the_vowels()
    test_get_positive_numbers()
    test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len()
    test_access_item_retrieves_item_when_passed_index_less_than_list_len()
