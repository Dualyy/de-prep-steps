import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE


"""
### get_even_nums ###

Write a function, get_even_nums, that takes an list of numbers (nums) and
returns a list of only the even numbers.

get_even_nums([1, 2, 3]) # returns [2]
"""


def get_even_nums(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens
    pass


@run_test
def get_even_nums_should_return_empty_list_when_no_numbers():
    assert get_even_nums([]) == [], format_err_msg([], get_even_nums([]))


@run_test
def get_even_nums_should_return_given_list_when_all_numbers_are_even():
    assert get_even_nums([2, 4, 6]) == [2, 4, 6], format_err_msg(
        [2, 4, 6], get_even_nums([2, 4, 6])
    )


@run_test
def get_even_nums_should_return_empty_list_when_all_numbers_are_odd():
    assert get_even_nums([1, 3, 5]) == [], format_err_msg([], get_even_nums([1, 3, 5]))


@run_test
def get_even_nums_should_return_list_of_just_even_numbers_when_numbers_are_mixed_even_and_odd():
    assert get_even_nums([1, 2, 3, 4, 5]) == [2, 4], format_err_msg(
        [2, 4], get_even_nums([1, 2, 3, 4, 5])
    )


"""
### get_items_longer_than ###

Write a function, get_items_longer_than, that takes a list of strings (strs)
and a length (max_len).
It should return an list of only the items longer than the given length.

get_items_longer_than(['a','bb','ccc'], 1) # returns ['bb', 'ccc'];

get_items_longer_than(['a','bb','ccc'], 2) # returns ['ccc'];

get_items_longer_than(['a','bb','ccc'], 4) # returns [];
"""


def get_items_longer_than(strs, max_len):
    longer = []
    for str in strs:
        if len(str) > max_len:
            longer.append(str)
    return longer
    pass


# ❗ Remember to change @skip_test to @run_test!
@run_test
def get_items_longer_than_should_return_empty_list_when_no_strings():
    assert get_items_longer_than([], 1) == [], format_err_msg(
        [], get_items_longer_than([], 1)
    )


@run_test
def get_items_longer_than_should_return_all_strings_longer_than_max_len():
    assert get_items_longer_than(["a", "bb"], 0) == ["a", "bb"], format_err_msg(
        ["a", "bb"], get_items_longer_than(["a", "bb"], 0)
    )


@run_test
def get_items_longer_than_should_exclude_strings_shorter_than_max_len():
    assert get_items_longer_than(["a", "bb"], 3) == [], format_err_msg(
        [], get_items_longer_than(["a", "bb"], 3)
    )


@run_test
def get_items_longer_than_should_exclude_strings_equal_to_max_len():
    assert get_items_longer_than(["a", "bb", "ccc"], 2) == ["ccc"], format_err_msg(
        ["ccc"], get_items_longer_than(["a", "bb", "ccc"], 2)
    )


"""
### get_sandwich_filling ###

Write a function, get_sandwich_filling, that takes a list of sandwich
ingredients (sandwich).
This list represents the ingredients used to make a sandwich, it's first and
last items will be the 'bread'
Return a list containing only the filling of the sandwich.

get_sandwich_filling(['bread', 'bacon', 'bread']) # returns ['bacon']

get_sandwich_filling(['bread', 'halluomi', 'lettuce', 'bread']) # returns
['halluomi', 'lettuce']

get_sandwich_filling(['a', 'b', 'c', 'd']) # returns ['b', 'c']
"""


def get_sandwich_filling(sandwich):
    return sandwich[1:-1]
    pass


@run_test
def get_sandwich_filling_should_return_list_with_single_filling():
    assert get_sandwich_filling(["bread", "lonely slice of cheese", "bread"]) == [
        "lonely slice of cheese"
    ], format_err_msg(
        ["lonely slice of cheese"],
        get_sandwich_filling(["bread", "lonely slice of cheese", "bread"]),
    )


@run_test
def get_sandwich_filling_should_return_list_with_multiple_fillings():
    assert get_sandwich_filling(
        ["bread", "tomato", "lettuce", "cheese", "patty", "bread"]
    ) == ["tomato", "lettuce", "cheese", "patty"], format_err_msg(
        ["tomato", "lettuce", "cheese", "patty"],
        get_sandwich_filling(
            ["bread", "tomato", "lettuce", "cheese", "patty", "bread"]
        ),
    )


@run_test
def get_sandwich_filling_should_return_empty_list_when_no_fillings():
    assert get_sandwich_filling(["bread", "bread"]) == [], format_err_msg(
        [], get_sandwich_filling(["bread", "bread"])
    )


"""
### remove_item ###

Write a function, remove_item, that takes a list (items) and a number (n).
Return a new list without the item at position n. This should be a new list and
the item should still exist in the original list

remove_item([1, 2, 3], 1) # returns [1, 3]

remove_item([3], 0) # returns []
"""


def remove_item(items, n):
    new_list = items[:]
    new_list.pop(n)
    return new_list
    pass


@run_test
def remove_item_should_return_list_with_specified_element_removed():
    assert remove_item([1], 0) == [], format_err_msg([], remove_item([1], 0))


@run_test
def remove_item_should_return_list_containing_all_elements_that_havent_been_removed():
    assert remove_item([1, 2, 3, 4, 5], 2) == [1, 2, 4, 5], format_err_msg(
        [1, 2, 4, 5], remove_item([1, 2, 3, 4, 5], 2)
    )


@run_test
def remove_item_should_only_remove_value_at_specified_index():
    assert remove_item([1, 2, 1, 2, 1], 2) == [1, 2, 2, 1], format_err_msg(
        [1, 2, 2, 1], remove_item([1, 2, 1, 2, 1], 2)
    )


@run_test
def remove_item_should_return_new_list():
    items = [1, 2, 3]
    result = remove_item(items, 2)
    assert result is not items, format_err_msg("a new list", "original input list")


@run_test
def remove_item_should_not_mutate_original_list():
    items = [1, 2, 3]
    remove_item(items, 2)
    assert items == [1, 2, 3], format_err_msg(
        "orginal list to be unchanged", "mutated input list"
    )


"""
### merge_lists ###

Write a function that takes two lists (list1 and list2) and
returns a new list with all of the elements of list1 followed by all of the
elements of list2.

The function should return a new list and both original lists should remain
unchanged.

merge_lists([1, 2], [3, 4]) # returns [1, 2, 3, 4]
"""


def merge_lists(list1, list2):
    return list1[:] + list2[:]
    pass


@run_test
def merge_lists_should_merge_two_single_element_lists_together():
    assert merge_lists([1], [2]) == [1, 2], format_err_msg(
        [1, 2], merge_lists([1], [2])
    )


@run_test
def merge_lists_should_merge_two_multi_element_lists_together():
    assert merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6], format_err_msg(
        [1, 2, 3, 4, 5, 6], merge_lists([1, 2, 3], [4, 5, 6])
    )


@run_test
def merge_lists_should_merge_two_lists_when_one_is_empty():
    assert merge_lists([1, 2, 3], []) == [1, 2, 3], format_err_msg(
        [1, 2, 3], merge_lists([1, 2, 3], [])
    )


@run_test
def merge_lists_should_merge_two_lists_when_both_are_empty():
    assert merge_lists([], []) == [], format_err_msg([], merge_lists([], []))


@run_test
def merge_lists_should_not_mutate_original_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merge_lists(list1, list2)
    assert list1 == [1, 2, 3], format_err_msg(
        "list 1 to be unchanged", "mutated input list 1"
    )
    assert list2 == [4, 5, 6], format_err_msg(
        "list 2 to be unchanged", "mutated input list 2"
    )


"""
### is_item_omnipresent ###

Write a function that takes an list of nested lists (lists) and an item to
check for (item).
It should return True if the passed item is present in every list inside lists.
Otherwise, it should return False.

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 3) # returns True, present in
all

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 9) # returns False, not
present in any

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 4) # returns False, only
present in two lists
"""


def is_item_omnipresent(lists, item):
    for list in lists:
        if item not in list:
            return False
    return True
    pass


@run_test
def is_item_omnipresent_should_return_false_if_item_is_missing_from_all_lists():
    assert is_item_omnipresent([[1], [2]], 3) is False, format_err_msg(
        False, is_item_omnipresent([[1], [2]], 3)
    )


@run_test
def is_item_omnipresent_should_return_false_if_item_is_missing_from_a_single_list():
    assert is_item_omnipresent([[1], [2]], 1) is False, format_err_msg(
        False, is_item_omnipresent([[1], [2]], 1)
    )


@run_test
def is_item_omnipresent_should_return_true_if_item_is_present_in_all_lists():
    assert is_item_omnipresent([[1], [1], [1]], 1) is True, format_err_msg(
        True, is_item_omnipresent([[1], [1], [1]], 1)
    )


@run_test
def is_item_omnipresent_should_return_true_if_item_is_present_amongst_other_elements_in_mixed_lists():
    assert is_item_omnipresent([[5, 4, 3, 2, 1], [1, 4, 4], [9, 1, 1]], 1) is True, (
        format_err_msg(
            True,
            is_item_omnipresent([[5, 4, 3, 2, 1], [1, 4, 4], [9, 1, 1]], 1),
        )
    )


"""
### flatten_lists ###

Write a function, flatten_list_by_one, that when given a list with one or more
nested lists (nested_lists) returns a new list with one less level of nesting.

All the elements of all the original nested lists must be kept in their
original order.

flatten_list_by_one([[1], [2], [3]])  # returns [1, 2, 3]

flatten_list_by_one([[1], [2], [[3, 4]]])  # returns [1, 2, [3, 4]]
"""


def flatten_list_by_one(nested_lists):
    new_lists = []
    for lists in nested_lists:
        if type(lists) == list:
            if len(lists) == 1 :
                new_lists.append(lists[0])
            else :
                for items in lists:
                    new_lists.append(items)
        else : new_lists.append(lists)
    return new_lists
    pass


@run_test
def flatten_list_by_one_should_remove_single_layer_of_nesting():
    assert flatten_list_by_one([[1], [2]]) == [1, 2], format_err_msg(
        [1, 2], flatten_list_by_one([[1], [2]])
    )


@run_test
def flatten_list_by_one_should_preserve_subsequent_layers_of_nesting():
    assert flatten_list_by_one([[[1, 2]], [[3, 4]]]) == [
        [1, 2],
        [3, 4],
    ], format_err_msg(
        [
            [1, 2],
            [3, 4],
        ],
        flatten_list_by_one(
            [
                [[1, 2]],
                [[3, 4]],
            ]
        ),
    )


@run_test
def flatten_list_by_one_should_combine_levels_of_nesting():
    assert flatten_list_by_one([[1, 2], [3, [4, 5]]]) == [
        1,
        2,
        3,
        [4, 5],
    ], format_err_msg([1, 2, 3, [4, 5]], flatten_list_by_one([[1, 2], [3, [4, 5]]]))


if __name__ == "__main__":
    get_even_nums_should_return_empty_list_when_no_numbers()
    get_even_nums_should_return_given_list_when_all_numbers_are_even()
    get_even_nums_should_return_empty_list_when_all_numbers_are_odd()
    get_even_nums_should_return_list_of_just_even_numbers_when_numbers_are_mixed_even_and_odd()
    get_items_longer_than_should_return_empty_list_when_no_strings()
    get_items_longer_than_should_return_all_strings_longer_than_max_len()
    get_items_longer_than_should_exclude_strings_shorter_than_max_len()
    get_items_longer_than_should_exclude_strings_equal_to_max_len()
    get_sandwich_filling_should_return_list_with_single_filling()
    get_sandwich_filling_should_return_list_with_multiple_fillings()
    get_sandwich_filling_should_return_empty_list_when_no_fillings()
    remove_item_should_return_list_with_specified_element_removed()
    remove_item_should_return_list_containing_all_elements_that_havent_been_removed()
    remove_item_should_only_remove_value_at_specified_index()
    remove_item_should_return_new_list()
    remove_item_should_not_mutate_original_list()
    merge_lists_should_merge_two_single_element_lists_together()
    merge_lists_should_merge_two_multi_element_lists_together()
    merge_lists_should_merge_two_lists_when_one_is_empty()
    merge_lists_should_merge_two_lists_when_both_are_empty()
    merge_lists_should_not_mutate_original_lists()
    is_item_omnipresent_should_return_false_if_item_is_missing_from_all_lists()
    is_item_omnipresent_should_return_false_if_item_is_missing_from_a_single_list()
    is_item_omnipresent_should_return_true_if_item_is_present_in_all_lists()
    is_item_omnipresent_should_return_true_if_item_is_present_amongst_other_elements_in_mixed_lists()
    flatten_list_by_one_should_remove_single_layer_of_nesting()
    flatten_list_by_one_should_preserve_subsequent_layers_of_nesting()
    flatten_list_by_one_should_combine_levels_of_nesting()
