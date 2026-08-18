import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE


# Challenge 0
# Write a function, check_if_key_exists, that takes a dictionary and a key as
#  its arguments
# It should return True if the dictionary contains the provided key,
#  False otherwise

def check_if_key_exists(dict,key):
    if key in dict:
        return True
    else: return False
pass

@run_test
def test_check_if_key_exists():
    assert (
        check_if_key_exists({"name": "jonny", "age": 32}, "name") is True
    ), format_err_msg(True, check_if_key_exists({"name": "jonny", "age": 32}, "name"))
    assert (
        check_if_key_exists({"name": "jonny", "age": 32}, "age") is True
    ), format_err_msg(True, check_if_key_exists({"name": "jonny", "age": 32}, "age"))
    assert (
        check_if_key_exists({"name": "jonny", "age": 32}, "pets") is False
    ), format_err_msg(False, check_if_key_exists({"name": "jonny", "age": 32}, "pets"))


# Challenge 1
# Write a function, create_dict, that takes a list consisting of two elements
#  representing a key / value pair as its argument
# It should return a dictionary with a single key based on the input

def create_dict(list):
    return {list[0]:list[1]}
    pass

@run_test
def test_create_dict():
    assert create_dict(["name", "shaq"]) == {"name": "shaq"}, format_err_msg(
        {"name": "shaq"}, create_dict(["name", "shaq"])
    )

    assert create_dict(["fruit", "apple"]) == {"fruit": "apple"}, format_err_msg(
        {"fruit": "apple"}, create_dict(["fruit", "apple"])
    )

    assert create_dict(["language", "haskell"]) == {
        "language": "haskell"
    }, format_err_msg({"language": "haskell"}, create_dict(["language", "haskell"]))


# Challenge 2
# Write a function, get_first_n_items, that takes two arguments, a list and
#  a number 'n'
# It should return a new list containing the first 'n' items of the given list

def get_first_n_items(items,n_items):
    return items[0:n_items]
    pass

@run_test
def test_get_first_n_items():
    assert get_first_n_items(["a", "b", "c", "d"], 2) == ["a", "b"], format_err_msg(
        ["a", "b"], get_first_n_items(["a", "b", "c", "d"], 2)
    )

    assert (
        get_first_n_items(["apple", "banana", "pear", "kiwi"], 0) == []
    ), format_err_msg([], get_first_n_items(["apple", "banana", "pear", "kiwi"], 0))

    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 3) == [
        "apple",
        "banana",
        "pear",
    ], format_err_msg(
        ["apple", "banana", "pear"],
        get_first_n_items(["apple", "banana", "pear", "kiwi"], 3),
    )


# Challenge 3
# Write a function, create_arrow, that takes a string representing a
#  direction ("left", "right", "up" or "down") as its argument
# It should return the corresponding arrow ("←", "→", "↑", "↓")
# You don't need to utilise an dictionary here, but think about how you
#  could do so

def create_arrow(direction):
    ARROWS = {"left":"←",
              "right": "→",
              "up": "↑",
              "down": "↓"}
    return ARROWS[direction]

@run_test
def test_create_arrow():
    assert create_arrow("left") == "←", format_err_msg("←", create_arrow("left"))
    assert create_arrow("right") == "→", format_err_msg("→", create_arrow("right"))
    assert create_arrow("up") == "↑", format_err_msg("↑", create_arrow("up"))
    assert create_arrow("down") == "↓", format_err_msg("↓", create_arrow("down"))


# Challenge 4
# Write a function, move_item_to_end, that takes two arguments, a list and an
#  index value
# It should return a new list where the item that was previously at the
#  given index is now at the end of the list

def move_item_to_end(itemlist,index):
    itemlist.append(itemlist[index])
    itemlist.pop(index)
    return itemlist
pass

@run_test
def test_move_item_to_end():
    assert move_item_to_end(["a", "b", "c"], 0) == ["b", "c", "a"], format_err_msg(
        ["b", "c", "a"], move_item_to_end(["a", "b", "c"], 0)
    )

    assert move_item_to_end(["a", "b", "c", "d"], 2) == [
        "a",
        "b",
        "d",
        "c",
    ], format_err_msg(["a", "b", "d", "c"], move_item_to_end(["a", "b", "c", "d"], 2))

    assert move_item_to_end(["a", "b", "c", "d"], 1) == [
        "a",
        "c",
        "d",
        "b",
    ], format_err_msg(["a", "c", "d", "b"], move_item_to_end(["a", "b", "c", "d"], 1))


# Challenge 5
# Write a function, update_user_age, that takes a dictionary representing a
#  user's account information
# A user object will look
# {
#       "admin": False,
#       "username": "xoxoAlexoxo",
#       "personal_details": {
#           "name": "Alex",
#           "age": 39,
#           "fav_food": "gooseberry fool"
#       },
# }
# The user's age should be increased by 1 to reflect their recent birthday
# NOTE: This function does NOT need to return anything!

def update_user_age(user):
    user["personal_details"]["age"] += 1

@run_test
def test_update_user_age():
    user1 = {
        "admin": False,
        "username": "xoxoAlexoxo",
        "personal_details": {
            "name": "Alex",
            "age": 39,
            "fav_food": "gooseberry fool",
        },
    }
    update_user_age(user1)
    assert user1 == {
        "admin": False,
        "username": "xoxoAlexoxo",
        "personal_details": {
            "name": "Alex",
            "age": 40,
            "fav_food": "gooseberry fool",
        },
    }, format_err_msg(
        {
            "admin": False,
            "username": "xoxoAlexoxo",
            "personal_details": {
                "name": "Alex",
                "age": 40,
                "fav_food": "gooseberry fool",
            },
        },
        user1,
    )

    user2 = {
        "admin": True,
        "username": "brum4life",
        "personal_details": {
            "name": "Poonam",
            "age": 19,
            "fav_food": "caviar",
        },
    }
    update_user_age(user2)
    assert user2 == {
        "admin": True,
        "username": "brum4life",
        "personal_details": {
            "name": "Poonam",
            "age": 20,
            "fav_food": "caviar",
        },
    }, format_err_msg(
        {
            "admin": True,
            "username": "brum4life",
            "personal_details": {
                "name": "Poonam",
                "age": 20,
                "fav_food": "caviar",
            },
        },
        user2,
    )


# Challenge 6
# Write a function, check_infinitive, that takes a string representing a
#  French word as an argument
# It should return True if it is an infinitive verb, and False otherwise
# A French infinitive verb is a word that ends with either "re", "ir" or "er"

def check_infinitive(word):
    WORD_ENDINGS = ["re", "ir","er"]
    if word[-2:] in WORD_ENDINGS:
        return True
    else: return False
pass
    


@run_test
def test_check_infinitive():
    assert check_infinitive("manger") is True, format_err_msg(
        True, check_infinitive("manger")
    )
    assert check_infinitive("faire") is True, format_err_msg(
        True, check_infinitive("faire")
    )
    assert check_infinitive("aller") is True, format_err_msg(
        True, check_infinitive("aller")
    )
    assert check_infinitive("finir") is True, format_err_msg(
        True, check_infinitive("finir")
    )
    assert check_infinitive("rendre") is True, format_err_msg(
        True, check_infinitive("rendre")
    )
    assert check_infinitive("savoir") is True, format_err_msg(
        True, check_infinitive("savoir")
    )

    assert check_infinitive("suis") is False, format_err_msg(
        False, check_infinitive("suis")
    )
    assert check_infinitive("ai") is False, format_err_msg(
        False, check_infinitive("ai")
    )
    assert check_infinitive("ete") is False, format_err_msg(
        False, check_infinitive("ete")
    )
    assert check_infinitive("sais") is False, format_err_msg(
        False, check_infinitive("sais")
    )
    assert check_infinitive("allons") is False, format_err_msg(
        False, check_infinitive("allons")
    )


# Challenge 7
# Write a function, collect_plurals, that takes a list of strings as
#  an argument
# It should return a list containing all strings ending with an 's' from the
#  input (retaining the order)

def collect_plurals(word_list):
    plurals =[]
    for word in word_list:
        if word.endswith('s'):
            plurals.append(word)
    return plurals

@run_test
def test_collect_plurals():
    assert collect_plurals(["dogs", "cat", "apples", "kittens", "kiwi"]) == [
        "dogs",
        "apples",
        "kittens",
    ], format_err_msg(
        ["dogs", "apples", "kittens"],
        collect_plurals(["dogs", "cat", "apples", "kittens", "kiwi"]),
    )

    assert collect_plurals(
        ["abcs", "humans", "thoughts", "cloud", "computer", "cups"]
    ) == ["abcs", "humans", "thoughts", "cups"], format_err_msg(
        ["abcs", "humans", "thoughts", "cups"],
        collect_plurals(["abcs", "humans", "thoughts", "cloud", "computer", "cups"]),
    )


# Challenge 8
# Write a function, make_all_admins, that takes a list of 'user' dictionaries
#  as an argument
# Each user will be an dictionary with key of 'name' and 'admin'
# The 'admin' key will have a boolean value
# You should return a list of user objects each with the 'admin' key set
#  to True

def make_all_admins(users):
    for user in users:
        if user["admin"] == False:
            user["admin"] = True
    return users


@run_test
def test_make_all_admins():
    users = [
        {"name": "Barry", "admin": False},
        {"name": "Sandeep", "admin": True},
        {"name": "Kavita", "admin": False},
    ]
    assert make_all_admins(users) == [
        {"name": "Barry", "admin": True},
        {"name": "Sandeep", "admin": True},
        {"name": "Kavita", "admin": True},
    ], format_err_msg(
        [
            {"name": "Barry", "admin": True},
            {"name": "Sandeep", "admin": True},
            {"name": "Kavita", "admin": True},
        ],
        make_all_admins(users),
    )


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":
    test_check_if_key_exists()
    test_create_dict()
    test_get_first_n_items()
    test_create_arrow()
    test_move_item_to_end()
    test_update_user_age()
    test_check_infinitive()
    test_collect_plurals()
    test_make_all_admins()
