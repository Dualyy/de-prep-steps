import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE


# Challenge 0
# This function should take a list as an argument and return True if the list
#  is empty, False otherwise.
def is_empty_list(input):
    return True if len(input) == 0 else False
    pass


@run_test
def test_is_empty_list():
    assert is_empty_list([]) is True, format_err_msg(True, is_empty_list([]))
    assert is_empty_list(["a", "b", "c", "d"]) is False, format_err_msg(
        False, is_empty_list(["a", "b", "c", "d"])
    )
    assert is_empty_list(["a"]) is False, format_err_msg(False, is_empty_list(["a"]))


# Challenge 1
# This function should take an dictionary representing a person and information
#  about whether they like to code

# A person will take this form:
# {
#   "name": "Mitch",
#   "likes_to_code": True
# }

# If the 'likes_to_code' key is true, then you should return a string of the
#   form "My name is Mitch and I like to code."


# If the 'likes_to_code' key is false, the string should look like
#   "My name is Mitch and I don't like to code."
def create_profile_description(person):
    if person["likes_to_code"] is True:
        return f"My name is {person["name"]} and I like to code."
    else:
        return f"My name is {person["name"]} and I don't like to code."
    pass


@run_test
def test_create_profile_description():
    assert (
        create_profile_description({"name": "Danika", "likes_to_code": True})
        == "My name is Danika and I like to code."
    ), format_err_msg(
        "My name is Danika and I like to code.",
        create_profile_description({"name": "Danika", "likes_to_code": True}),
    )
    assert (
        create_profile_description({"name": "Alex", "likes_to_code": False})
        == "My name is Alex and I don't like to code."
    ), format_err_msg(
        "My name is Alex and I don't like to code.",
        create_profile_description({"name": "Alex", "likes_to_code": False}),
    )


# Challenge 2
# This function should take a string representing a traffic light colour as
#  an argument

# It will be one of "red", "green" or "amber" in either uppercase or lowercase
# You should return a corresponding message


def read_traffic_light(traffic_light):
    lower_traffic_light = traffic_light.lower()

    match lower_traffic_light:
        case "red":
            return "STOP!"
        case "amber":
            return "GET READY..."
        case "green":
            return "GO!"
    pass


@run_test
def test_read_traffic_light():
    assert read_traffic_light("green") == "GO!", format_err_msg(
        "GO!", read_traffic_light("green")
    )
    assert read_traffic_light("GREEN") == "GO!", format_err_msg(
        "GO!", read_traffic_light("GREEN")
    )

    assert read_traffic_light("amber") == "GET READY...", format_err_msg(
        "GET READY...", read_traffic_light("amber")
    )
    assert read_traffic_light("AMBER") == "GET READY...", format_err_msg(
        "GET READY...", read_traffic_light("AMBER")
    )

    assert read_traffic_light("red") == "STOP!", format_err_msg(
        "STOP!", read_traffic_light("red")
    )
    assert read_traffic_light("RED") == "STOP!", format_err_msg(
        "STOP!", read_traffic_light("RED")
    )


# Challenge 3
# This function should take any number of arguments and return the number of
#  arguments passed into the function
def how_many_arguments(*args):
    list_of_args = [*args]
    return len(list_of_args)
    pass


@run_test
def test_how_many_arguments():
    assert how_many_arguments("a", "b", "c") == 3, format_err_msg(
        3, how_many_arguments("a", "b", "c")
    )
    assert how_many_arguments() == 0, format_err_msg(0, how_many_arguments())
    assert how_many_arguments(1, 2, 3, 4, 5) == 5, format_err_msg(
        5, how_many_arguments(1, 2, 3, 4, 5)
    )
    assert (
        how_many_arguments("the", "meaning", "of", "life", "is", 42) == 6
    ), format_err_msg(8, how_many_arguments("the", "meaning", "of", "life", "is", 42))


# Challenge 4
# This function should take a dictionary representing a coin machine and a
#  string representing a coin as its arguments

# A coin machine object will take this form:
# {
#   "1p": 0,
#   "2p": 0,
#   "5p": 0,
#   "10p": 0
# }


# You should 'add the provided coin to the machine by altering the associated
#  key and returning the updated coin machine
def update_coin_machine(coin_machine,coin):
    if coin in coin_machine:
        coin_machine[coin] += 1
        return coin_machine
    else: return coin_machine
    pass


@run_test
def test_update_coin_machine():
    assert update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p") == {
        "1p": 1,
        "2p": 0,
        "5p": 0,
        "10p": 0,
    }, format_err_msg(
        {"1p": 1, "2p": 0, "5p": 0, "10p": 0},
        update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p"),
    )
    assert update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p") == {
        "1p": 0,
        "2p": 1,
        "5p": 0,
        "10p": 0,
    }, format_err_msg(
        {"1p": 0, "2p": 1, "5p": 0, "10p": 0},
        update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p"),
    )

    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p") == {
        "1p": 0,
        "2p": 4,
        "5p": 0,
        "10p": 0,
    }, format_err_msg(
        {"1p": 0, "2p": 4, "5p": 0, "10p": 0},
        update_coin_machine({"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p"),
    )

    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p") == {
        "1p": 0,
        "2p": 3,
        "5p": 11,
        "10p": 0,
    }, format_err_msg(
        {"1p": 0, "2p": 3, "5p": 11, "10p": 0},
        update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p"),
    )

    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p") == {
        "1p": 0,
        "2p": 3,
        "5p": 10,
        "10p": 1,
    }, format_err_msg(
        {"1p": 0, "2p": 3, "5p": 10, "10p": 1},
        update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p"),
    )


# Challenge 5

# This function should take a list representing coordinates - an x position and
#  a y position - and a string representing a direction.
# It should return a new pair of coordinates, with the coords updated by moving
#  either x or y 1 unit in a particular direction.


# If direction is "up" it should move 1 unit up (+ 1 in the y direction)
# If the direction is "down" it should move 1 unit down (-1 in the y direction)
# If the direction is "right" it should move 1 unit right
#   (+1 in the x direction)
# If the direction is "left" it should move 1 unit left (-1 in the x direction)
def update_position(coordinates,direction):
    match direction:
        case "up":
            coordinates[1] += 1
            return coordinates
        case "down":
            coordinates[1] -= 1
            return coordinates
        case "left":
            coordinates[0] -= 1
            return coordinates
        case "right":
            coordinates[0] += 1
            return coordinates
    pass


@run_test
def test_update_position():
    assert update_position([10, 10], "up") == [10, 11], format_err_msg(
        [10, 11], update_position([10, 10], "up")
    )

    assert update_position([0, 0], "down") == [0, -1], format_err_msg(
        [0, -1], update_position([0, 0], "down")
    )

    assert update_position([3, 3], "left") == [2, 3], format_err_msg(
        [2, 3], update_position([3, 3], "left")
    )

    assert update_position([7, 50], "right") == [8, 50], format_err_msg(
        [8, 50], update_position([7, 50], "right")
    )


# Challenge 6
# This function should take any value as an argument, and return true if it is
#  falsy, and false otherwise
def is_falsy(input):
    return True if bool(input) == False else False
    pass


@run_test
def test_is_falsy():
    assert is_falsy(False) is True, format_err_msg(True, is_falsy(False))
    assert is_falsy(True) is False, format_err_msg(False, is_falsy(True))
    assert is_falsy("") is True, format_err_msg(True, is_falsy(""))
    assert is_falsy(0) is True, format_err_msg(True, is_falsy(0))
    assert is_falsy({}) is True, format_err_msg(True, is_falsy({}))
    assert is_falsy({"a": 1}) is False, format_err_msg(False, is_falsy({"a": 1}))
    assert is_falsy([]) is True, format_err_msg(True, is_falsy([]))
    assert is_falsy([1, 2, 3]) is False, format_err_msg(False, is_falsy([1, 2, 3]))
    assert is_falsy(None) is True, format_err_msg(True, is_falsy(None))


# Challenge 7
# This function should take a number representing a dice roll and a string
#  representing a coin toss as its arguments
# A dice roll will be a number between 1 and 6
# A coin toss will be "H" or "T" representing heads or tails
# The game is considered to be won if the dice roll is 3 or higher AND the
#  coin toss is "H"
# You should return True if the game has been won and False otherwise
def check_game(dice,coin):
    if dice >= 3 and coin == 'H':
        return True
    else: return False

    pass


@run_test
def test_check_game():
    assert check_game(3, "H") is True, format_err_msg(True, check_game(3, "H"))
    assert check_game(4, "H") is True, format_err_msg(True, check_game(4, "H"))
    assert check_game(5, "H") is True, format_err_msg(True, check_game(5, "H"))
    assert check_game(6, "H") is True, format_err_msg(True, check_game(6, "H"))
    assert check_game(6, "T") is False, format_err_msg(False, check_game(6, "T"))


# Challenge 8
# In this function, a "coin collection" is represented by a list containing 4
#  other nested lists, each representing a slot in the collection in the
#  following way:
#        1p   2p   5p   10p
#       [[],  [],  [],  []] <-- coin collection
# This should take two arguments, a coin collection list and a
#   string representing a coin, and return an updated version of the given
#   list with the coin added at the appropriate position
def add_coins(coin_collection,coins):
    match coins:
        case "1p":
            coin_collection[0] += [coins]
        case "2p":
            coin_collection[1] += [coins]
        case "5p":
            coin_collection[2] += [coins]
        case "10p":
            coin_collection[3] += [coins]
    return coin_collection
    pass


@run_test
def test_add_coins():
    assert add_coins([[], [], [], []], "1p") == [["1p"], [], [], []], format_err_msg(
        [["1p"], [], [], []], add_coins([[], [], [], []], "1p")
    )

    assert add_coins([[], [], [], []], "2p") == [[], ["2p"], [], []], format_err_msg(
        [[], ["2p"], [], []], add_coins([[], [], [], []], "2p")
    )

    assert add_coins([[], ["2p"], [], []], "2p") == [
        [],
        ["2p", "2p"],
        [],
        [],
    ], format_err_msg([[], ["2p", "2p"], [], []], add_coins([[], ["2p"], [], []], "2p"))

    assert add_coins([[], [], [], []], "5p") == [[], [], ["5p"], []], format_err_msg(
        [[], [], ["5p"], []], add_coins([[], [], [], []], "5p")
    )

    assert add_coins([["1p"], [], [], ["10p", "10p"]], "2p") == [
        ["1p"],
        ["2p"],
        [],
        ["10p", "10p"],
    ], format_err_msg(
        [["1p"], ["2p"], [], ["10p", "10p"]],
        add_coins([["1p"], [], [], ["10p", "10p"]], "2p"),
    )

    assert add_coins([[], [], ["5p", "5p"], []], "5p") == [
        [],
        [],
        ["5p", "5p", "5p"],
        [],
    ], format_err_msg(
        [[], [], ["5p", "5p", "5p"], []], add_coins([[], [], ["5p", "5p"], []], "5p")
    )


# Mark your progress on the Learn 2 Code platform before moving on to the
#  next set of challenges!


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":
    test_is_empty_list()
    test_create_profile_description()
    test_read_traffic_light()
    test_how_many_arguments()
    test_update_coin_machine()
    test_update_position()
    test_is_falsy()
    test_check_game()
    test_add_coins()
