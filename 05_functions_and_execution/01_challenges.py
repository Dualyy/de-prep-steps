import os  
import sys  

sys.path.append(os.getcwd())  

from test_api.checks import run_test, skip_test

# DO NOT CHANGE CODE ABOVE THIS LINE


# Challenge 0
@run_test
def test_multi_type_list():
    multi_type_list = ["I am a string", 42, True, [1, 2, 3]]

    assert type(multi_type_list[0]) == str
    assert type(multi_type_list[1]) == int
    assert type(multi_type_list[2]) == bool
    assert type(multi_type_list[3]) == list


# Challenge 1
@run_test
def test_list_mutation():
    letters = ["a", "b", "c"]
    letters.append("d")
    letters.append("g")

    assert letters == ["a", "b", "c","d","g"]

    last_letter = letters.pop()

    assert last_letter == "g"
    assert letters == ["a", "b", "c","d"]


# Challenge 2
@run_test
def test_nested_lists():
    rows = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
    ]

    assert rows[0] == ["a", "b", "c"]
    assert rows[1] == ["d", "e", "f"]
    assert rows[2] == ["g", "h", "i"]

    first_row = rows[0]
    assert first_row[0] == "a"
    assert first_row[1] == "b"

    assert rows[1][1] == "e"
    assert rows[2][0] == "g"
    assert rows[0][2] == "c"


# Challenge 3
@run_test
def test_dictionary_keys():
    father = {
        "first_name": "Michael",
        "last_name": "Bluth",
        "age": 33,
    }

    key = "first_name"
    assert father["last_name"] == "Bluth"
    assert father["age"] == 33
    assert father[key] == "Michael"


# Challenge 4
@run_test
def test_removing_dict_keys():
    brother_in_law = {
        "name": "Tobias",
        "lastname": "Funke",
        "job": "therapist",
    }

    assert brother_in_law["job"] == "therapist"

    del brother_in_law["job"]
    assert brother_in_law == {
        "name": "Tobias",
        "lastname": "Funke",
    }


# Challenge 5
@run_test
def test_nested_dictionaries():
    bluth_family = {
        "father": {
            "name": "George",
        },
        "mother": {
            "name": "Lucille",
        },
        "sons": [{"name": "GOB"}, {"name": "Michael"}, {"name": "Buster"}],
        "daughters": [{"name": "Lindsay"}],
    }

    assert bluth_family["father"]["name"] == "George"
    assert bluth_family["mother"]["name"] == "Lucille"
    assert bluth_family["daughters"][0]["name"] == "Lindsay"


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":
    test_multi_type_list()
    test_list_mutation()
    test_nested_lists()
    test_dictionary_keys()
    test_removing_dict_keys()
    test_nested_dictionaries()
