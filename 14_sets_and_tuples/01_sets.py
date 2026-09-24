import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg, NORMAL_RED, DEFAULT

# DO NOT CHANGE CODE ABOVE THIS LINE

# Task 1
def create_set(numbers):
    """
    This function should take a list of numbers and convert it to a set
    """
    return {number for number in numbers}

    pass


@run_test
def test_create_set():
    assert create_set([1, 2, 3, 4]) == {1, 2, 3, 4}, \
        format_err_msg({1, 2, 3, 4}, create_set([1, 2, 3, 4]))

    assert create_set([5, 6, 7, 8]) == {5, 6, 7, 8}, \
        format_err_msg({5, 6, 7, 8}, create_set([5, 6, 7, 8]))

    assert create_set([45, 87, 12, 1]) == {45, 87, 12, 1}, \
        format_err_msg({45, 87, 12, 1}, create_set([45, 87, 12, 1]))

    assert create_set([1, 1, 2, 3, 3]) == {1, 2, 3}, \
        format_err_msg({1, 2, 3}, create_set([1, 1, 2, 3, 3]))


# Task 2
def is_in_set(my_set, element):
    """
    This function should take a set and an element and return True if the set
    contains the element and False otherwise
    """

    return True if element in my_set else False
    pass


@run_test
def test_is_in_set():
    assert is_in_set({5, 2, 3, 4}, 1) is False, \
        format_err_msg(False, is_in_set({5, 2, 3, 4}, 1))

    assert is_in_set({'a', 'b', 'c', 'd'}, 'a') is True, \
        format_err_msg(True, is_in_set({'a', 'b', 'c', 'd'}, 'a'))


# Task 3
def remove_set_element(my_set):
    """
    This function should take a set, remove any one element from it and return
    the removed element
    """
    return my_set.pop()

    pass 


@run_test
def test_remove_set_element():
    test_set = {1, 2, 3, 4, 5}
    removed_element = remove_set_element(test_set)

    # Check if the function has returned one of the elements in the set
    assert removed_element in [1, 2, 3, 4, 5], \
        format_err_msg(True, removed_element in [1, 2, 3, 4, 5])

    # Check if an element has been removed from the set
    assert len(test_set) == 4, format_err_msg(4, len(test_set))


# Task 4
def discard_set_element(my_set, value):
    """
    This function should take a set and a value. It should remove the
    specified value from the set and return the original set.
    """
    my_set.remove(value)

    return my_set
    pass


@run_test
def test_discard_set_element():
    assert discard_set_element(
        {"help", "fix", "my", "code"}, "help") == {"fix", "my", "code"}, \
        format_err_msg(
        {"fix", "my", "code"},
        discard_set_element({"help", "fix", "my", "code"}, "help"))

    input = {"I", "bug", "love", "coding"}
    assert discard_set_element(input, "bug") is input, \
        f"{NORMAL_RED}function should return the same set{DEFAULT}"


# Task 5
def copy_set(my_set):
    """
    This function should take a set and return a *new copy* of that set
    """
    copy_set = my_set.copy()

    return copy_set

    pass


@run_test
def test_copy_set():
    assert copy_set({1, 2, 3}) == {1, 2, 3}, \
        format_err_msg({1, 2, 3}, copy_set({1, 2, 3}))

    # check that the function returns a new set
    input = {1, 2, 3}
    assert copy_set(input) is not input, \
        f"{NORMAL_RED}function should return a copy of the given set{DEFAULT}"


# Do not change the code below this line
if __name__ == "__main__":
    test_create_set()
    test_is_in_set()
    test_remove_set_element()
    test_discard_set_element()
    test_copy_set()