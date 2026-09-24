import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

#  Task 1
def check_common_values(set_1, set_2):
    """
    This function should take two sets and check if they have any elements in
        common.
    - If they DO share any common elements then the function should return True
    - If they DON'T share any common elements then the function should return
        False
    """
    return True if set_1.intersection(set_2) != set() else False

    pass


@run_test
def test_check_common_values():
    assert check_common_values({1, 2, 3}, {2, 3, 4}) is True, \
        format_err_msg(True, check_common_values({1, 2, 3}, {2, 3, 4}))

    assert check_common_values({"a", "b", "c"}, {"x", "y", "z"}) is False, \
        format_err_msg(False, check_common_values(
            {"a", "b", "c"}, {"x", "y", "z"}))


# Task 2
def check_subset(set_1, set_2):
    """
    This function should take two sets, set_1 and set_2, if set_2 is a
    *subset* of set_1 then the function should return true.

    A subset is a set made up of values contained in the set it is being
    compared to.
    E.g.
    {3,4} is a *subset* of {1,2,3,4,5}
    """

    return True if set_2.issubset(set_1) else False
    pass


@run_test
def test_check_subset():
    assert check_subset({'a', 'b', 'c'}, {'a'}) is True, \
        format_err_msg(True, check_subset({'a', 'b', 'c'}, {'a'}))

    assert check_subset({1, 2, 3}, {5, 6}) is False, \
        format_err_msg(False, check_subset({1, 2, 3}, {5, 6}))


# Task 3
def check_superset(set_1, set_2):
    """
    This function should take two sets, set_1 and set_2, if set_2 is a
    *superset* of set_1 then the function should return true.

    A superset is a set that includes all the values contained in the set
    it is being compared to.
    E.g.
    {1,2,3,4,5} is a *superset* of {3,4}
    """
    return True if set_2.issuperset(set_1) else False

    pass


@run_test
def test_check_superset():
    assert check_superset({1, 2}, {1, 2, 3, 4, 5}) is True, \
        format_err_msg(True, check_superset({1, 2}, {1, 2, 3, 4, 5}))

    assert check_superset({1, 2, 3, 4, 5}, {1, 2, 3}) is False, \
        format_err_msg(False, check_superset({1, 2, 3, 4, 5}, {1, 2, 3}))

    assert check_superset({'a', 'b', 'c'}, {1, 2, 3}) is False, \
        format_err_msg(False, check_superset({'a', 'b', 'c'}, {1, 2, 3}))


# Task 4
def find_set_differences(set_1, set_2):
    """
    This function should take two sets, set_1 and set_2.

    It should return a set containing all the elements of set_1 that aren't
    in set_2 AND all the elements of set_2 that aren't in set_1.
    """
    return set_2.symmetric_difference(set_1)


@run_test
def test_find_set_differences():
    set_1 = {"laptop", "phone", "glasses", "lunch"}
    set_2 = {"phone", "keys", "wallet", "lunch"}
    assert find_set_differences(set_1, set_2) == \
        {"wallet", "laptop", "keys", "glasses"}, \
        format_err_msg({"wallet", "laptop", "keys", "glasses"},
                       find_set_differences(set_1, set_2))

    set_3 = {1, 2, 3, 4, 5}
    set_4 = {5, 6, 7, 1}
    assert find_set_differences(set_3, set_4) == {2, 3, 4, 6, 7}, \
        format_err_msg({2, 3, 4, 6, 7}, find_set_differences(set_3, set_4))

    set_5 = {1, 2, 3, "data", 4, 5}
    set_6 = {"we", 3, "love", 2, "data"}
    assert find_set_differences(set_5, set_6) == {1, 4, 5, "love", "we"}, \
        format_err_msg({1, 4, 5, "love", "we"},
                       find_set_differences(set_5, set_6))


# Task 5
def create_union(set_1, set_2):
    """
    This function should create a *union* of set_1 and set_2. A union will
    have all the values of both sets. There will be no duplicates.
    """
    return set_1.union(set_2)
    pass


@run_test
def test_create_union():
    set_1 = {"laptop", "phone", "glasses", "lunch"}
    set_2 = {"phone", "keys", "wallet", "lunch"}
    expected = {"phone", "glasses", "lunch", "wallet", "laptop", "keys"}
    assert create_union(set_1, set_2) == expected, \
        format_err_msg(expected, create_union(set_1, set_2))

    set_3 = {1, 2, 3, 4, 5}
    set_4 = {5, 6, 7, 1}
    expected = {1, 2, 3, 4, 5, 6, 7}
    assert create_union(set_3, set_4) == expected, \
        format_err_msg(expected, create_union(set_3, set_4))

    set_5 = {1, 2, 3, "data", 4, 5}
    set_6 = {"we", 3, "love", 2, "data"}
    expected = {1, 2, 3, 4, 5, "we", "love", "data"}
    assert create_union(set_5, set_6) == expected, \
        format_err_msg(expected, create_union(set_5, set_6))

# Task 6


def create_intersection(set_1, set_2):
    """
    This function should create an *intersection* of set_1 and set_2. An
    intersection will contain all the values that are present in BOTH sets.
    """
    return set_1.intersection(set_2)
    pass


@run_test
def test_create_intersection():
    set_1 = {"laptop", "phone", "glasses", "lunch"}
    set_2 = {"phone", "keys", "wallet", "lunch"}
    assert create_intersection(set_1, set_2) == {"phone", "lunch"}, \
        format_err_msg({"phone", "lunch"}, create_intersection(set_1, set_2))

    set_3 = {1, 2, 3, 4, 5}
    set_4 = {5, 6, 7, 1}
    assert create_intersection(set_3, set_4) == {1, 5}, \
        format_err_msg({1, 5}, create_union(set_3, set_4))

    set_5 = {1, 2, 3, "data", 4, 5}
    set_6 = {"we", 3, "love", 2, "data"}
    assert create_intersection(set_5, set_6) == {2, 3, "data"}, \
        format_err_msg({2, 3, "data"}, create_union(set_5, set_6))


# Do not change the code below this line
if __name__ == "__main__":
    test_check_common_values()
    test_check_subset()
    test_check_superset()
    test_find_set_differences()
    test_create_union()
    test_create_intersection()