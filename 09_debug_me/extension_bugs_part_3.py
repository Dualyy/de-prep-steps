import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

"""
### count_occurrences ###

`count_occurrences` is a function that takes a list and a value.
It should return a number representing 
the total number of times that the value appears in the list.

Unfortunately, it looks like the function isn't working.

Can you work out what needs changing to make the function pass all the tests?
"""


def count_occurrences(list_to_check, value):
    count = 0
    for i in range(len(list_to_check)):
        if list_to_check[i] == value:
            count += 1
    return count


# Do not change tests!

@run_test
def count_occurrences_should_return_0_if_no_match_empty_list():
    result = count_occurrences([], "a")
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def count_occurrences_should_return_0_if_no_match_non_empty_list():
    result = count_occurrences(["a", "b", "c"], "d")
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def count_occurrences_should_count_occurrences_in_simple_list():
    result = count_occurrences(["a", "b", "c"], "b")
    expected = 1
    assert result == expected, format_err_msg(expected, result)


@run_test
def count_occurrences_should_count_occurrences_in_mixed_list():
    result = count_occurrences(
        ["1", "a", 2, "2", "b", 1, "a", "1", "2", "c", 3, "2", 2], 2
    )
    expected = 2
    assert result == expected, format_err_msg(expected, result)


"""
### add_guests_to_party ###

`add_guests_to_party` is a function that takes
a list of `invitee` dictionaries.

It should check whether each of these objects has an
'RSVP' key with a value of 'yes'.

If the invitee has RSVP'd, then we should add them to the `guests` list on the
`party` dictionary in our function,and then return the `guests` list.

Unfortunately, it looks like the function isn't working.

Can you work out what needs changing to make the function pass all the tests?

(An `invitee` might look like this: `{'name': 'Simon', 'RSVP': 'no'}`).
"""


def add_guests_to_party(invitees):
    party = {
        'host': 'Paul Copley Esq',
        'venue': 'The Ritzy Bar',
        'theme': 'Heroes of Code',
        'guests': [
            {
                'name': 'Cat'
            },
            {
                'name': 'Kyle'
            }
        ]
    }
    for invitee in invitees:
        if invitee['RSVP'] == 'yes':
            party["guests"].append({'name': invitee['name']})
    return party["guests"]


# Do not change tests!

@run_test
def add_guests_to_party_should_return_a_list():
    result = add_guests_to_party([])
    expected = []
    assert isinstance(result, list), format_err_msg(expected, result)


@run_test
def add_guests_to_party_should_return_unchanged_guestlist_if_no_invitees():
    result = add_guests_to_party([])
    expected = [{"name": "Cat"}, {"name": "Kyle"}]
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_guests_to_party_should_return_unchanged_guestlist_if_NO_RSVPs():
    result = add_guests_to_party(
        [{"name": "Chon", "RSVP": "no"}, {"name": "Verity", "RSVP": "no"}]
    )
    expected = [{"name": "Cat"}, {"name": "Kyle"}]
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_guests_to_party_should_return_new_guests_if_ALL_RSVP_yes():
    result = add_guests_to_party(
        [{"name": "Liam", "RSVP": "yes"}, {"name": "Haz", "RSVP": "yes"}]
    )
    expected = [{"name": "Cat"}, {"name": "Kyle"}, {"name": "Liam"}, {"name": "Haz"}]
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_guests_to_party_should_return_new_guests_if_SOME_RSVP_yes():
    result = add_guests_to_party(
        [
            {"name": "Sarah", "RSVP": "yes"},
            {"name": "Jim", "RSVP": "no"},
            {"name": "Emily", "RSVP": "yes"},
            {"name": "Dominic", "RSVP": "yes"},
        ]
    )
    expected = [
        {"name": "Cat"},
        {"name": "Kyle"},
        {"name": "Sarah"},
        {"name": "Emily"},
        {"name": "Dominic"},
    ]
    assert result == expected, format_err_msg(expected, result)

if __name__ == "__main__":
    count_occurrences_should_return_0_if_no_match_empty_list()
    count_occurrences_should_return_0_if_no_match_non_empty_list()
    count_occurrences_should_count_occurrences_in_simple_list()
    count_occurrences_should_count_occurrences_in_mixed_list()

    add_guests_to_party_should_return_a_list()
    add_guests_to_party_should_return_unchanged_guestlist_if_no_invitees()
    add_guests_to_party_should_return_unchanged_guestlist_if_NO_RSVPs()
    add_guests_to_party_should_return_new_guests_if_ALL_RSVP_yes()
    add_guests_to_party_should_return_new_guests_if_SOME_RSVP_yes()