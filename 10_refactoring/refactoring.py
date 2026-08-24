import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

"""
### triple_nums ###

`triple_nums` is a function that takes a list of numbers and returns a list
containing the result of multiplying each of those numbers by 3.

Refactor triple_nums to use a _list comprehension_ instead of a for loop.

For advice on how to do this, check out the following:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions:~:text=5.1.3.%20List%20Comprehensions-,%C2%B6,-List%20comprehensions%20provide

Or the following guide on SpeedSheet: https://speedsheet.io/s/python#gL31

If you run python on this file, all tests should pass.
"""


def triple_nums(nums):
    # tripled = []
    # for i in range(len(nums)):
    #     tripled.append(3 * nums[i])
    return [num * 3 for num in nums]


# Do not change tests!


@run_test
def triple_nums_should_return_list():
    result = triple_nums([])
    expected = []
    assert isinstance(result, list), format_err_msg(expected, result)


@run_test
def triple_nums_should_return_empty_list_when_passed_empty_list():
    result = triple_nums([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def triple_nums_should_return_list_of_all_numbers_multiplied_by_three():
    result = triple_nums([10, 25, 30, 40])
    expected = [30, 75, 90, 120]
    assert result == expected, format_err_msg(expected, result)


"""
### shout_names ###

`shout_names` is a function that takes a list of names and returns a list
containing all of the names in capital letters followed by an
exclamation mark "!".

Refactor `shout_names` to use a list comprehension.

If you run python on this file, all tests should pass.
"""


def shout_names(names):
    # shouted_names = []
    # for name in names:
    #     shouted_names.append(name.upper() + "!")
    return [name.upper() + "!" for name in names]


# Do not change tests!


@run_test
def shout_names_should_return_a_list():
    result = shout_names([])
    expected = []
    assert isinstance(result, list), format_err_msg(expected, result)


@run_test
def shout_names_should_return_empty_list_when_passed_empty_list():
    result = shout_names([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def shout_names_should_shout_names():
    result = shout_names(["Carrie", "Diya", "Kyle", "Christian"])
    expected = ["CARRIE!", "DIYA!", "KYLE!", "CHRISTIAN!"]
    assert result == expected, format_err_msg(expected, result)


"""
### is_sweet_enough ###

is_sweet_enough is a function that takes a list of food items and returns
either True or False depending on whether every food in the array has a
sweet flavour.

Refactor is_sweet_enough to use a for comprehension with the `all` function:
https://speedsheet.io/s/python#PEU2

The food items look like this: {'name': 'chocolate', 'flavour': 'sweet'}

If you run python on this file, all tests should pass.
"""


def is_sweet_enough(food_items):
    # for i in range(len(food_items)):
    #     if food_items[i]["flavour"] != "sweet":
    #         return False
    IS_NOT_SWEET = False
    IS_SWEET = not IS_NOT_SWEET

    return IS_SWEET if all([IS_NOT_SWEET for item in food_items if item["flavour"] != "sweet"]) else IS_NOT_SWEET


    


# Do not change tests!


@run_test
def is_sweet_enough_should_return_true_when_all_foods_are_sweet():
    result = is_sweet_enough(
        [
            {"name": "chocolate", "flavour": "sweet"},
            {"name": "banana", "flavour": "sweet"},
            {"name": "barfi", "flavour": "sweet"},
        ]
    )
    expected = True
    assert result == expected, format_err_msg(expected, result)


@run_test
def is_sweet_enough_should_return_false_when_no_foods_are_sweet():
    result = is_sweet_enough(
        [
            {"name": "samosa", "flavour": "savoury"},
            {"name": "lemon", "flavour": "sour"},
            {"name": "olive", "flavour": "bitter"},
        ]
    )
    expected = False
    assert result == expected, format_err_msg(expected, result)


@run_test
def is_sweet_enough_should_return_false_when_any_foods_are_not_sweet():
    result = is_sweet_enough(
        [
            {"name": "stollen", "flavour": "sweet"},
            {"name": "cranberries", "flavour": "sour"},
            {"name": "mince pie", "flavour": "sweet"},
        ]
    )
    expected = False
    assert result == expected, format_err_msg(expected, result)


"""
### get_excited ###

`get_excited` is a function that takes a piece of text and returns it with all
of the full stops (.) replaced by exclamation marks (!).

Refactor get_excited to use a string method. All of this code can be rewritten
in just one line with one string method...

If you run python on this file, all tests should pass.
"""


def get_excited(text):
    
    return text.replace(".", "!")


@run_test
def get_excited_should_return_empty_string_when_passed_empty_string():
    result = get_excited("")
    expected = ""
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_excited_should_return_unchanged_string_when_no_full_stops_present():
    result = get_excited("the quick brown fox jumps over the lazy dog")
    expected = "the quick brown fox jumps over the lazy dog"
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_excited_should_replace_full_stops_with_exclamation_marks_single_full_stop():
    result = get_excited("We're gonna need a bigger boat.")
    expected = "We're gonna need a bigger boat!"
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_excited_should_replace_full_stops_with_exclamation_marks_multiple_full_stops():
    result = get_excited("Woo. Woo. Woo. Who's ready to code?")
    expected = "Woo! Woo! Woo! Who's ready to code?"
    assert result == expected, format_err_msg(expected, result)


"""
### shrek_characters ###

shrek_characters is a function that takes a list of movie characters and
returns a list of only the characters from the film franchise, Shrek.

Refactor shrek_characters to use a comprehension.

If you run python on this file, all tests should pass.
"""


def shrek_characters(characters):
    # shreks = []
    # for character in characters:
    #     if "Shrek" in character["movie"]:
    #         shreks.append(character["name"])
    # return shreks

    return [character["name"] for character in characters if character["movie"] is "Shrek"]


# Do not change tests!


@run_test
def shrek_characters_should_return_empty_list_when_passed_empty_list():
    result = shrek_characters([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def shrek_characters_should_return_empty_list_when_no_shrek_characters():
    result = shrek_characters(
        [
            {"name": "Cedric Diggory", "movie": "Harry Potter and the Goblet of Fire"},
            {"name": "Elle Woods", "movie": "Legally Blonde"},
            {"name": "Paddington Bear", "movie": "Paddington 2"},
        ]
    )
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def shrek_characters_should_return_list_of_shrek_characters():
    result = shrek_characters(
        [
            {"name": "Shrek", "movie": "Shrek"},
            {"name": "Lord Farquaad", "movie": "Shrek"},
            {"name": "Magic Mirror", "movie": "Shrek"},
        ]
    )
    expected = ["Shrek", "Lord Farquaad", "Magic Mirror"]
    assert result == expected, format_err_msg(expected, result)


if __name__ == "__main__":
    triple_nums_should_return_list()
    triple_nums_should_return_empty_list_when_passed_empty_list()
    triple_nums_should_return_list_of_all_numbers_multiplied_by_three()

    shout_names_should_return_a_list()
    shout_names_should_return_empty_list_when_passed_empty_list()
    shout_names_should_shout_names()

    is_sweet_enough_should_return_true_when_all_foods_are_sweet()
    is_sweet_enough_should_return_false_when_no_foods_are_sweet()
    is_sweet_enough_should_return_false_when_any_foods_are_not_sweet()

    get_excited_should_return_empty_string_when_passed_empty_string()
    get_excited_should_return_unchanged_string_when_no_full_stops_present()
    get_excited_should_replace_full_stops_with_exclamation_marks_single_full_stop()
    get_excited_should_replace_full_stops_with_exclamation_marks_multiple_full_stops()

    shrek_characters_should_return_empty_list_when_passed_empty_list()
    shrek_characters_should_return_empty_list_when_no_shrek_characters()
    shrek_characters_should_return_list_of_shrek_characters()
