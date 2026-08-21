import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

"""
Write a function that takes a list of booleans (`bools`) and returns a `list`
with all of their values swapped
such that `True` becomes `False` and `False` becomes `True`.


flip_booleans([True, True, True]) # returns [False, False, False]

flip_booleans([False, False, False]) # returns [True, True, True]

flip_booleans([True, False, False, True]) # returns [False, True, True, False]

flip_booleans([]) # returns []

"""

def flip_booleans(bools):

    for i in range(len(bools)):
        bools[i]= not bools[i]
    return bools
    pass


@run_test
def flip_booleans_should_return_empty_list_when_passed_empty_list():
    result = flip_booleans([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def flip_booleans_should_return_single_false_when_passed_single_true():
    result = flip_booleans([True])
    expected = [False]
    assert result == expected, format_err_msg(expected, result)


@run_test
def flip_booleans_should_return_single_true_when_passed_single_false():
    result = flip_booleans([False])
    expected = [True]
    assert result == expected, format_err_msg(expected, result)


@run_test
def flip_booleans_should_return_all_false_when_passed_all_true():
    result = flip_booleans([True, True, True])
    expected = [False, False, False]
    assert result == expected, format_err_msg(expected, result)


@run_test
def flip_booleans_should_return_all_true_when_passed_all_false():
    result = flip_booleans([False, False, False])
    expected = [True, True, True]
    assert result == expected, format_err_msg(expected, result)


@run_test
def flip_booleans_should_return_mixed_true_and_false_flipped_correctly():
    result = flip_booleans([True, False, False, True])
    expected = [False, True, True, False]
    assert result == expected, format_err_msg(expected, result)


"""
Northcoders is expanding to France!

Unfortunately for us, our team on the ground in Paris are patriotically
Francophone and have been providing us with student data partly in French.

Write a function that will take a dictionary representing a student's data, a
key that needs changing, and its English translation.

The function should return a new dictionary with the relevant key name changed
to its English translation.

If the key to change does not exist in the student then no changes should be
made.

student = {
    'prénom': 'Carla',
    'surname': 'Bruni',
    'job': 'Artist'
}

translate_key(student, 'prénom', 'first_name') # should return the following:

{
    'first_name': 'Carla',
    'surname': 'Bruni',
    'job': 'Artist'
}

"""


def translate_key(student, key_to_change, translation):
    if key_to_change in student:
        student[translation] = student[key_to_change]
        del student[key_to_change] 
    return student
    pass


@run_test
def translate_key_should_return_empty_dictionary_when_passed_empty_dictionary():
    result = translate_key({}, "prénom", "first_name")
    expected = {}
    assert result == expected, format_err_msg(expected, result)


@run_test
def translate_key_should_return_unchanged_if_key_not_present():
    result = translate_key(
        {"first_name": "Carla", "surname": "Bruni", "job": "Artist"},
        "prénom",
        "first_name",
    )
    expected = {"first_name": "Carla", "surname": "Bruni", "job": "Artist"}
    assert result == expected, format_err_msg(expected, result)


@run_test
def translate_key_should_return_new_dictionary_with_key_translated():
    result = translate_key(
        {"prénom": "Carla", "surname": "Bruni", "job": "Artist"}, "prénom", "first_name"
    )
    expected = {"first_name": "Carla", "surname": "Bruni", "job": "Artist"}
    assert result == expected, format_err_msg(expected, result)


@run_test
def translate_key_should_return_new_dictionary():
    result = translate_key(
        {"first_name": "Jean", "surname": "Reno", "emploi": "Actor"}, "emploi", "job"
    )
    expected = {"first_name": "Jean", "surname": "Reno", "job": "Actor"}
    assert result is not expected, format_err_msg("new dictionary", "input dictionary")


"""
Write a function that takes a list of people dictionaries (`people`) and
returns the first person dictionary in the list that has the `'is_dentist'`
property set to `True`. If no dentists are included in the `people` list,
the function should return `None`.

find_first_dentist([]) # returns None

find_first_dentist([{'name': 'Callum', 'is_dentist': False}]) # returns None

find_first_dentist([{'name': 'Callum', 'is_dentist': False},
{'name': 'Carrie', 'is_dentist': True}])
# returns {'name': 'Carrie', 'is_dentist': True}

find_first_dentist([{'name': 'Callum', 'is_dentist': True},
{'name': 'Carrie', 'is_dentist': True}])
# returns {'name': 'Callum', 'is_dentist': True}

"""


def find_first_dentist(people):
    for person in people:
        if person["is_dentist"] == True:
            return person

    return None
    pass


@run_test
def find_first_dentist_should_return_none_when_passed_empty_list():
    result = find_first_dentist([])
    expected = None
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_first_dentist_should_return_none_if_person_not_dentist():
    result = find_first_dentist([{"name": "Callum", "is_dentist": False}])
    expected = None
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_first_dentist_should_return_person_if_dentist():
    result = find_first_dentist([{"name": "Callum", "is_dentist": True}])
    expected = {"name": "Callum", "is_dentist": True}
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_first_dentist_should_return_first_dentist():
    result = find_first_dentist(
        [
            {"name": "Callum", "is_dentist": False},
            {"name": "Carrie", "is_dentist": True},
        ]
    )
    expected = {"name": "Carrie", "is_dentist": True}
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_first_dentist_should_return_first_dentist_of_many():
    result = find_first_dentist(
        [
            {"name": "Callum", "is_dentist": True},
            {"name": "Carrie", "is_dentist": True},
        ]
    )
    expected = {"name": "Callum", "is_dentist": True}
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a list of `people` dictionaries in the format:

[
    {
        'name': 'Emmeline',
        'lives': {
            'country': 'UK',
            'city': 'Manchester'
        },
        'age': 32
    }
]


The function should return the number of people who live in the
city of Manchester.

tally_people_in_manchester([{
    'name': 'Emmeline',
    'lives': { 'country': 'UK', 'city': 'Manchester' },
    'age': 32
    }]) # returns 1

tally_people_in_manchester([{
    'name': 'Carrie',
    'lives': { 'country': 'UK', 'city': 'Leeds' },
    'age': 32
    }]) # returns 0

tally_people_in_manchester([
    {
    'name': 'Carrie',
    'lives': { 'country': 'UK', 'city': 'Leeds' },
    'age': 32
    },
    { 'name': 'Ray',
    'lives': { 'country': 'UK', 'city': 'Manchester' },
    'age': 31
    }
    ]) # returns 1

tally_people_in_manchester([]) # returns 0

"""


def tally_people_in_manchester(people):
    count = 0

    for person in people:
        if person["lives"]["city"] == 'Manchester':
            count += 1

    return count
    pass


@run_test
def tally_people_in_manchester_should_return_0_when_passed_empty_list():
    result = tally_people_in_manchester([])
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_people_in_manchester_should_return_0_when_no_one_in_manchester():
    result = tally_people_in_manchester(
        [
            {
                "name": "Carrie",
                "lives": {"country": "UK", "city": "Leeds"},
                "age": 32,
            }
        ]
    )
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_people_in_manchester_should_return_1_when_one_person_in_manchester():
    result = tally_people_in_manchester(
        [
            {
                "name": "Emmeline",
                "lives": {"country": "UK", "city": "Manchester"},
                "age": 32,
            }
        ]
    )
    expected = 1
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_people_in_manchester_should_return_number_of_people_in_manchester_when_passed_multiple():
    result = tally_people_in_manchester(
        [
            {
                "name": "Carrie",
                "lives": {"country": "UK", "city": "Leeds"},
                "age": 32,
            },
            {
                "name": "Ray",
                "lives": {"country": "UK", "city": "Manchester"},
                "age": 31,
            },
            {
                "name": "Simon",
                "lives": {"country": "Middle Earth", "city": "Moria"},
                "age": 275,
            },
            {
                "name": "Cat",
                "lives": {"country": "UK", "city": "Manchester"},
                "age": 42,
            },
            {
                "name": "Danika",
                "lives": {"country": "UK", "city": "Manchester"},
                "age": 22,
            },
        ]
    )
    expected = 3
    assert result == expected, format_err_msg(expected, result)


"""
Write a function takes a list of dictionaries describing `dogs` and returns a
list of the names of all the pug owners.


get_pug_owners([
    {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
    {'name': 'Max', 'breed': 'Pug', 'owner': 'Izzi'},
    {'name': 'Poppy', 'breed': 'Pug', 'owner': 'Anat'}
]) # returns ['Izzi', 'Anat']

get_pug_owners([
    {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
]) # returns []

get_pug_owners([]) # returns []
"""


def get_pug_owners(dogs):
    owners = []
    for dog in dogs:
        if dog['breed'] == 'Pug':
            owners.append(dog['owner'])
    return owners

    pass


@run_test
def get_pug_owners_should_return_empty_list_when_passed_empty_list():
    result = get_pug_owners([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_pug_owners_should_return_empty_list_when_no_pugs():
    result = get_pug_owners(
        [
            {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
        ]
    )
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_pug_owners_should_return_single_pug_owner():
    result = get_pug_owners(
        [
            {"name": "Beatrice", "breed": "Pug", "owner": "Tom"},
        ]
    )
    expected = ["Tom"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_pug_owners_should_return_multiple_pug_owners():
    result = get_pug_owners(
        [
            {"name": "Max", "breed": "Pug", "owner": "Izzi"},
            {"name": "Poppy", "breed": "Pug", "owner": "Anat"},
        ]
    )
    expected = ["Izzi", "Anat"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_pug_owners_should_return_mixed_list():
    result = get_pug_owners(
        [
            {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
            {"name": "Max", "breed": "Pug", "owner": "Izzi"},
            {"name": "Poppy", "breed": "Pug", "owner": "Anat"},
        ]
    )
    expected = ["Izzi", "Anat"]
    assert result == expected, format_err_msg(expected, result)


"""
In this function, you will be provided with a dictionary. That dictionary is
storing information on keys:

{
    'name': 'Tom',
    'job': ['writing katas', 'marking'],
    'favourite_shop': [
        "Paul's Donkey University",
        "Shaq's Taxidermy Shack",
        "Sam's Pet Shop"
    ]
}

In some cases, however, the keys have been very badly named. Good naming
convention tells us that the __keys containing lists__ should have
plural names.
This function should return a new dictionary that is a copy of the input but
with any keys that contain lists pluralised (an 's' added to the end.)

{
    'name': 'Tom',
    'jobs': ['writing katas', 'marking'],
    'favourite_shops': [
        "Paul's Donkey University",
        "Shaq's Taxidermy Shack",
        "Sam's Pet Shop"
    ]
}
"""


def pluralise_keys(dictionary):
    dic = dictionary.copy()
    for item in dictionary:
        if item.endswith('s') is False and type(dictionary[item]) is list:
            dic[item + 's'] = dic[item]
            del dic[item]
    return dic
    pass


@run_test
def pluralise_keys_should_return_empty_dictionary_when_passed_empty_dictionary():
    result = pluralise_keys({})
    expected = {}
    assert result == expected, format_err_msg(expected, result)


@run_test
def pluralise_keys_should_return_unchanged_dictionary_when_there_are_no_lists():
    test_dict = {"a": 1, "b": 2, "c": 3}
    result = pluralise_keys(test_dict)
    expected = {"a": 1, "b": 2, "c": 3}
    assert result == expected, format_err_msg(expected, result)


@run_test
def pluralise_keys_should_return_copy_of_dictionary_when_there_are_no_lists():
    test_dict = {"a": 1, "b": 2, "c": 3}
    result = pluralise_keys(test_dict)
    assert result is not test_dict, format_err_msg(
        "new dictionary returned", "input dictionary returned"
    )


@run_test
def pluralise_keys_should_return_unchanged_dictionary_with_nested_dicts():
    test_dict = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
    result = pluralise_keys(test_dict)
    expected = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
    assert result == expected, format_err_msg(expected, result)


@run_test
def pluralise_keys_should_return_copy_of_dictionary_with_nested_dicts():
    test_dict = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
    result = pluralise_keys(test_dict)
    assert result is not test_dict, format_err_msg("new dictionary", "input dictionary")


@run_test
def pluralise_keys_should_return_dictionary_with_one_key_changed():
    test_dict = {"a": 1, "b": 2, "num": [3, 4]}
    result = pluralise_keys(test_dict)
    expected = {"a": 1, "b": 2, "nums": [3, 4]}
    assert result == expected, format_err_msg(expected, result)


@run_test
def pluralise_keys_should_return_copy_of_dictionary_with_one_nested_list():
    test_dict = {"a": 1, "b": 2, "num": [3, 4]}
    result = pluralise_keys(test_dict)
    assert result is not test_dict, format_err_msg("new dictionary", "input dictionary")


@run_test
def pluralise_keys_should_return_dictionary_with_several_keys_changed():
    test_dict = {
        "name": "Tom",
        "job": ["writing katas", "marking"],
        "favourite_shop": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ],
    }
    result = pluralise_keys(test_dict)
    expected = {
        "name": "Tom",
        "jobs": ["writing katas", "marking"],
        "favourite_shops": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ],
    }
    assert result == expected, format_err_msg(expected, result)


@run_test
def pluralise_keys_should_return_copy_of_dictionary_with_several_lists():
    test_dict = {
        "name": "Tom",
        "job": ["writing katas", "marking"],
        "favourite_shop": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ],
    }
    result = pluralise_keys(test_dict)
    assert result is not test_dict, format_err_msg("new dictionary", "input dictionary")


"""
Write a function that takes a `string` and returns a list containing the
length of each word in that string.
If passed an empty string, the function should return an empty list.
Words will be separated by a single space.


get_word_lengths('hello') # returns [5]

get_word_lengths('hello everyone') # returns [5, 8]

get_word_lengths('this is a sentence') # returns [4, 2, 1, 8]

get_word_lengths('') # returns []

"""


def get_word_lengths(string):
    if len(string) > 1:
        split = string.split(' ')
        return [len(word) for word in split]
    else:
        return []
    pass


@run_test
def get_word_lengths_should_return_empty_list_when_passed_empty_string():
    result = get_word_lengths("")
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_word_lengths_should_return_single_word_length():
    result = get_word_lengths("hello")
    expected = [5]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_word_lengths_should_return_two_word_lengths():
    result = get_word_lengths("hello everyone")
    expected = [5, 8]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_word_lengths_should_return_multiple_word_lengths():
    result = get_word_lengths("It is a pleasure to meet you new coder")
    expected = [2, 2, 1, 8, 2, 4, 3, 3, 5]
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a list of `words` and returns a list containing
all of the words that are
palindromes (the same word forwards and backwards, e.g. 'pip').


get_palindromes(['racecar']) # returns ['racecar']

get_palindromes(['dog', 'dud', 'car', 'mum']) # returns ['dud', 'mum']

get_palindromes(['apple', 'orange', 'banana']) # returns []

get_palindromes([]) # returns []

"""


def get_palindromes(words):
    return[word for word in words if word[::-1] == word]
    pass


@run_test
def get_palindromes_should_return_empty_list_when_passed_empty_list():
    result = get_palindromes([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_palindromes_should_return_empty_list_when_passed_no_palindromes():
    result = get_palindromes(["boom"])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_palindromes_should_return_single_palindrome():
    result = get_palindromes(["racecar"])
    expected = ["racecar"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_palindromes_should_return_multiple_palindromes_from_assorted_list():
    result = get_palindromes(["dog", "dud", "car", "mum"])
    expected = ["dud", "mum"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_palindromes_should_return_empty_list_when_no_palindromes_in_list():
    result = get_palindromes(["apple", "orange", "banana"])
    expected = []
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a `string` and returns a string with all of the
letter characters replaced with an 'X'.
Any non-letter characters (e.g. punctuation, symbols) should be left as they
are.

replace_letters_with_x('a') # returns 'X'

replace_letters_with_x('A') # returns 'X'

replace_letters_with_x('hello') # returns 'XXXXX'

replace_letters_with_x('Hello!') # returns 'XXXXX!'

replace_letters_with_x('Do you like coding?') # returns 'XX XXX XXXX XXXXXX?'

"""


def replace_letters_with_x(string):
    dic = 'abcdefghijklmnoprstuvwxyz'
    split = string.split(' ')
    if string == "":
        return string
    for index, word in enumerate(split):
        new_word = ""
        for char in word:
            if char in dic or char in dic.upper():
                new_word += 'X'  
            else:
                new_word += char
        split[index] = new_word
    return ' '.join(split)
    pass


@run_test
def replace_letters_with_x_should_return_empty_string_when_passed_empty_string():
    result = replace_letters_with_x("")
    expected = ""
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_non_letter_character():
    result = replace_letters_with_x("5")
    expected = "5"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_special_character():
    result = replace_letters_with_x("&")
    expected = "&"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_letter_changed_to_X():
    result = replace_letters_with_x("a")
    expected = "X"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_letter_changed_to_X_uppercase():
    result = replace_letters_with_x("K")
    expected = "X"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_word_changed_to_X():
    result = replace_letters_with_x("hello")
    expected = "XXXXX"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_word_changed_to_X_mixed_case():
    result = replace_letters_with_x("NoRtHcOdErS")
    expected = "XXXXXXXXXXX"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_word_changed_to_X_with_punctuation_exclamation_mark():
    result = replace_letters_with_x("Kaboom!")
    expected = "XXXXXX!"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_single_word_changed_to_X_with_punctuation_question_mark():
    result = replace_letters_with_x("Northcoders?")
    expected = "XXXXXXXXXXX?"
    assert result == expected, format_err_msg(expected, result)


@run_test
def replace_letters_with_x_should_return_several_words():
    result = replace_letters_with_x("Do you like coding?")
    expected = "XX XXX XXXX XXXXXX?"
    assert result == expected, format_err_msg(expected, result)


if __name__ == "__main__":
    flip_booleans_should_return_empty_list_when_passed_empty_list()
    flip_booleans_should_return_single_false_when_passed_single_true()
    flip_booleans_should_return_single_true_when_passed_single_false()
    flip_booleans_should_return_all_false_when_passed_all_true()
    flip_booleans_should_return_all_true_when_passed_all_false()
    flip_booleans_should_return_mixed_true_and_false_flipped_correctly()

    translate_key_should_return_empty_dictionary_when_passed_empty_dictionary()
    translate_key_should_return_unchanged_if_key_not_present()
    translate_key_should_return_new_dictionary_with_key_translated()
    translate_key_should_return_new_dictionary()

    find_first_dentist_should_return_none_when_passed_empty_list()
    find_first_dentist_should_return_none_if_person_not_dentist()
    find_first_dentist_should_return_person_if_dentist()
    find_first_dentist_should_return_first_dentist()
    find_first_dentist_should_return_first_dentist_of_many()

    tally_people_in_manchester_should_return_0_when_passed_empty_list()
    tally_people_in_manchester_should_return_0_when_no_one_in_manchester()
    tally_people_in_manchester_should_return_1_when_one_person_in_manchester()
    tally_people_in_manchester_should_return_number_of_people_in_manchester_when_passed_multiple()

    get_pug_owners_should_return_empty_list_when_passed_empty_list()
    get_pug_owners_should_return_empty_list_when_no_pugs()
    get_pug_owners_should_return_single_pug_owner()
    get_pug_owners_should_return_multiple_pug_owners()
    get_pug_owners_should_return_mixed_list()

    pluralise_keys_should_return_empty_dictionary_when_passed_empty_dictionary()
    pluralise_keys_should_return_unchanged_dictionary_when_there_are_no_lists()
    pluralise_keys_should_return_copy_of_dictionary_when_there_are_no_lists()
    pluralise_keys_should_return_unchanged_dictionary_with_nested_dicts()
    pluralise_keys_should_return_copy_of_dictionary_with_nested_dicts()
    pluralise_keys_should_return_dictionary_with_one_key_changed()
    pluralise_keys_should_return_copy_of_dictionary_with_one_nested_list()
    pluralise_keys_should_return_dictionary_with_several_keys_changed()
    pluralise_keys_should_return_copy_of_dictionary_with_several_lists()

    get_word_lengths_should_return_empty_list_when_passed_empty_string()
    get_word_lengths_should_return_single_word_length()
    get_word_lengths_should_return_two_word_lengths()
    get_word_lengths_should_return_multiple_word_lengths()

    get_palindromes_should_return_empty_list_when_passed_empty_list()
    get_palindromes_should_return_empty_list_when_passed_no_palindromes()
    get_palindromes_should_return_single_palindrome()
    get_palindromes_should_return_multiple_palindromes_from_assorted_list()
    get_palindromes_should_return_empty_list_when_no_palindromes_in_list()

    replace_letters_with_x_should_return_empty_string_when_passed_empty_string()
    replace_letters_with_x_should_return_single_non_letter_character()
    replace_letters_with_x_should_return_single_special_character()
    replace_letters_with_x_should_return_single_letter_changed_to_X()
    replace_letters_with_x_should_return_single_letter_changed_to_X_uppercase()
    replace_letters_with_x_should_return_single_word_changed_to_X()
    replace_letters_with_x_should_return_single_word_changed_to_X_mixed_case()
    replace_letters_with_x_should_return_single_word_changed_to_X_with_punctuation_exclamation_mark()
    replace_letters_with_x_should_return_single_word_changed_to_X_with_punctuation_question_mark()
    replace_letters_with_x_should_return_several_words()
