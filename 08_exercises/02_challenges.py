import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

"""
Write a function that takes a string of a mobile number (`mobile_number`).
It should return `True` if the number is a valid UK number and `False` if not.

A valid mobile number may begin with:

1. '07' followed by 9 more digits.
2. '+447' followed by 9 more digits.
3. '00447' followed by 9 more digits.

Anything else is `invalid`.

is_valid_mobile_number('07726') # returns False

is_valid_mobile_number('07123456789') # returns True

is_valid_mobile_number('+447123456789') # returns True

is_valid_mobile_number('00447123456789') # returns True

is_valid_mobile_number('0712345678!') # returns False
"""


def is_valid_mobile_number(mobile_number):
    valid_number_start = ['07','+447','00447']
    SPECIAL_CHARACTERS = '"!@#$%^&*()-+?_=,<>/"'
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    if any(char in mobile_number[1:] for char in ALPHABET):
        return False
    if any(char in mobile_number[1:] for char in SPECIAL_CHARACTERS):
        return False

    for number_start in valid_number_start:
        if len(mobile_number) - len(number_start) == 9:
            if mobile_number.startswith(number_start):
                return True
    return False

    pass


@run_test
def test_empty_string_invalid():
    assert is_valid_mobile_number("") is False, format_err_msg(
        False, is_valid_mobile_number("")
    )


@run_test
def test_length_less_than_eleven_is_invalid():
    assert is_valid_mobile_number("0754321") is False, format_err_msg(
        False, is_valid_mobile_number("0754321")
    )


@run_test
def test_length_more_than_fourteen_invalid():
    assert is_valid_mobile_number("004471234567890") is False, format_err_msg(
        False, is_valid_mobile_number("004471234567890")
    )


@run_test
def test_valid_examples_length_eleven():
    assert is_valid_mobile_number("07123456789") is True, format_err_msg(
        True, is_valid_mobile_number("07123456789")
    )
    assert is_valid_mobile_number("07284619462") is True, format_err_msg(
        True, is_valid_mobile_number("07284619462")
    )


@run_test
def test_invalid_examples_length_eleven():
    assert is_valid_mobile_number("+4471234567") is False, format_err_msg(
        False, is_valid_mobile_number("+4471234567")
    )
    assert is_valid_mobile_number("00447876543") is False, format_err_msg(
        False, is_valid_mobile_number("00447876543")
    )


@run_test
def test_length_twelve_invalid():
    assert is_valid_mobile_number("071234567890") is False, format_err_msg(
        False, is_valid_mobile_number("071234567890")
    )


@run_test
def test_valid_examples_length_thirteen():
    assert is_valid_mobile_number("+447123456789") is True, format_err_msg(
        True, is_valid_mobile_number("+447123456789")
    )
    assert is_valid_mobile_number("+447395612859") is True, format_err_msg(
        True, is_valid_mobile_number("+447395612859")
    )


@run_test
def test_invalid_examples_length_thirteen():
    assert is_valid_mobile_number("0044712345678") is False, format_err_msg(
        False, is_valid_mobile_number("0044712345678")
    )
    assert is_valid_mobile_number("0739561285901") is False, format_err_msg(
        False, is_valid_mobile_number("0739561285901")
    )


@run_test
def test_valid_examples_length_fourteen():
    assert is_valid_mobile_number("00447123456789") is True, format_err_msg(
        True, is_valid_mobile_number("00447123456789")
    )
    assert is_valid_mobile_number("00447654297190") is True, format_err_msg(
        True, is_valid_mobile_number("00447654297190")
    )


@run_test
def test_invalid_examples_length_fourteen():
    assert is_valid_mobile_number("+4471234567890") is False, format_err_msg(
        False, is_valid_mobile_number("+4471234567890")
    )
    assert is_valid_mobile_number("07102938475610") is False, format_err_msg(
        False, is_valid_mobile_number("07102938475610")
    )


@run_test
def test_invalid_if_contains_non_numeric_characters_other_than_first():
    assert is_valid_mobile_number("0728461a462") is False, format_err_msg(
        False, is_valid_mobile_number("0728461a462")
    )
    assert is_valid_mobile_number("+4473956+2859") is False, format_err_msg(
        False, is_valid_mobile_number("+4473956+2859")
    )
    assert is_valid_mobile_number("00447123!56789") is False, format_err_msg(
        False, is_valid_mobile_number("00447123!56789")
    )


"""
Write a function that takes a `string` and `adds` all the numbers in the
string together.
The function should then return this total as an integer.

Consecutive numbers should be treated as individual digits
(e.g. '123' is the same as 1, 2, 3 and not 123).

sum_digits_from_string('1') # returns 1

sum_digits_from_string('168') # returns 15

sum_digits_from_string('he12ll3') # returns 6

sum_digits_from_string('northcoders') # returns 0

"""


def sum_digits_from_string(string):

    NUMBERS = "0123456789"

    if any(num in string for num in NUMBERS):

        number_list = list(string)
        results = []

        for index, item in enumerate(number_list):

            if any(num in item for num in NUMBERS):
                results.append(int(item))

        return sum(results)


    else: return 0
    pass


@run_test
def sum_digits_from_string_should_return_0_for_empty_string():
    result = sum_digits_from_string("")
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def sum_digits_from_string_should_return_0_for_non_numeric_string():
    result = sum_digits_from_string("a")
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def sum_digits_from_string_should_return_integer_for_single_digit():
    result = sum_digits_from_string("5")
    expected = 5
    assert result == expected, format_err_msg(expected, result)


@run_test
def sum_digits_from_string_should_return_sum_for_two_digits():
    result = sum_digits_from_string("16")
    expected = 7
    assert result == expected, format_err_msg(expected, result)


@run_test
def sum_digits_from_string_should_return_sum_for_three_digits():
    result = sum_digits_from_string("255")
    expected = 12
    assert result == expected, format_err_msg(expected, result)


@run_test
def sum_digits_from_string_should_return_sum_for_mixed_string():
    result = sum_digits_from_string("he12ll3")
    expected = 6
    assert result == expected, format_err_msg(expected, result)


@run_test
def sum_digits_from_string_should_return_0_for_no_numbers():
    result = sum_digits_from_string("northcoders")
    expected = 0
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a list of `names` representing a person's full
name and returns a list
of each person whose last name is 'Williams'.


get_williams(['David Williams']) # returns ['David Williams']

get_williams(['David Williams', 'Sarah Williams'])
# returns ['David Williams', 'Sarah Williams']

get_williams(['Kirsty February']) # returns []

get_williams(['Kirsty February', 'Sam Williams']) # returns ['Sam Williams']

get_williams(['William David', 'Cole Williamson']) # returns []

"""


def get_williams(names):

    williams  = []
    for name in names:
        if name[-8::] == "Williams": # -8 is len of "Williams"
            williams.append(name)
    return williams

    pass


@run_test
def get_williams_should_return_empty_list_for_empty_list():
    result = get_williams([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_williams_should_return_empty_list_for_single_invalid_item():
    result = get_williams(["Kirsty February"])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_williams_should_return_single_valid_item():
    result = get_williams(["David Williams"])
    expected = ["David Williams"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_williams_should_return_several_valid_items():
    result = get_williams(["David Williams", "Sarah Williams"])
    expected = ["David Williams", "Sarah Williams"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_williams_should_return_mixed_items():
    result = get_williams(["Kirsty February", "Sam Williams"])
    expected = ["Sam Williams"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_williams_should_return_empty_list_for_mixed_items_with_rogue_williams():
    result = get_williams(["William David", "Cole Williamson"])
    expected = []
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a list of `numbers` and returns a list containing
the factorial of each number in the list.

The factorial of a number is the product of that number and all the integers
below it.
E.g. the factorial of 4 is 4 * 3 * 2 * 1 = 24


get_factorials([3]) # returns [6]

get_factorials([3, 4]) # returns [6, 24]

get_factorials([1, 5, 2]) # returns [1, 120, 2]

get_factorials([]) # returns []

"""


def get_factorials(numbers):

    results = []
    new_num = []
    factorial = None

    for num in numbers:
        factor = None
        new_num = list(range(1,num +1)) # we do not want 0 in the array so we go from 1 to num+1 

        for item in new_num:
            if factor == None:
                factor = item
            else:
                factor *= item

        results.append(factor)

    return results


    pass


@run_test
def get_factorials_should_return_empty_list_for_empty_list():
    result = get_factorials([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_factorials_should_return_single_item():
    result = get_factorials([3])
    expected = [6]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_factorials_should_return_multiple_items():
    result = get_factorials([1, 5, 2])
    expected = [1, 120, 2]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_factorials_should_return_factorial_of_1():
    result = get_factorials([1])
    expected = [1]
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a `number` and returns the largest number that can
be made by rearranging the digits.

largest_number(3) # returns 3

largest_number(123) # returns 321

largest_number(937846) # returns 987643

largest_number(43) # returns 43

"""


def largest_number(number):
    result = ""
    list = sorted(str(number), reverse = True)

    for item in list:
        result += item
    if(result == ""):
        return number
    else:
        return int(result)
    pass


@run_test
def largest_number_should_return_single_digit():
    result = largest_number(3)
    expected = 3
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_double_digits_in_correct_order():
    result = largest_number(43)
    expected = 43
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_double_digits_in_incorrect_order():
    result = largest_number(34)
    expected = 43
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_double_digits_repeated():
    result = largest_number(44)
    expected = 44
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_triple_digits_in_correct_order():
    result = largest_number(321)
    expected = 321
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_triple_digits_in_incorrect_order():
    result = largest_number(213)
    expected = 321
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_triple_digits_with_two_repeated():
    result = largest_number(233)
    expected = 332
    assert result == expected, format_err_msg(expected, result)


@run_test
def largest_number_should_return_lots_of_digits():
    result = largest_number(8456329456)
    expected = 9866554432
    assert result == expected, format_err_msg(expected, result)


"""
Write a function that takes a `number` and returns a matrix of nested lists
equal to the number passed.
Each element in each sublist should be set to a value of `None`.


generate_matrix(1) # returns [[None]]

generate_matrix(2) # returns [[None, None], [None, None]]

generate_matrix(3) # returns [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

"""


def generate_matrix(number):
    matrix = []
    for x in range(number):
        matrix.append([None] * number)
    return matrix
    pass


@run_test
def generate_matrix_should_return_empty_list_for_zero():
    result = generate_matrix(0)
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def generate_matrix_should_return_single_nested_list_for_single_digit():
    result = generate_matrix(1)
    expected = [[None]]
    assert result == expected, format_err_msg(expected, result)


@run_test
def generate_matrix_should_return_two_nested_lists_for_two_digits():
    result = generate_matrix(2)
    expected = [[None, None], [None, None]]
    assert result == expected, format_err_msg(expected, result)


@run_test
def generate_matrix_should_return_three_nested_lists_for_three_digits():
    result = generate_matrix(3)
    expected = [[None, None, None], [None, None, None], [None, None, None]]
    assert result == expected, format_err_msg(expected, result)


"""
This function takes a list of fruit (`orchard`) in the format:


['apple', 'apple', 'apple', 'apple', 'elppa', 'apple']


The fruit will all be the 'right way round' apart from one fruit!

Your function should return its zero-based index position.
So in this example, the function should return 4.

Note: The fruit will not always be apple, but it will always be an orchard
of the same kind of fruit.


find_wrong_way_fruit(['apple', 'apple', 'elppa']) # returns 2

find_wrong_way_fruit(['apple', 'elppa', 'apple']) # returns 1

find_wrong_way_fruit(['banana', 'ananab', 'banana', 'banana']) # returns 1

find_wrong_way_fruit(['apple', 'elppa']) # returns 0 as we can't tell which
one is the right way round with less than 3 pieces of fruit

"""


def find_wrong_way_fruit(orchard):
    fruits = {}
    #counts occurences of each item
    for index, fruit in enumerate(orchard):
        fruits[fruit] = orchard.count(fruit)
    #since we know only 1 reversed fruit we can return
    for key,value in fruits.items():
        if value == 1:
            return orchard.index(key)
    
    return 0
    pass


@run_test
def find_wrong_way_fruit_should_return_zero_for_singleton_list():
    result = find_wrong_way_fruit(["apple"])
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_wrong_way_fruit_should_return_zero_for_list_length_two():
    result = find_wrong_way_fruit(["grape", "eparg"])
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_wrong_way_fruit_should_find_last_item_if_reversed():
    result = find_wrong_way_fruit(["apple", "apple", "elppa"])
    expected = 2
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_wrong_way_fruit_should_find_first_item_if_reversed():
    result = find_wrong_way_fruit(["elppa", "apple", "apple"])
    expected = 0
    assert result == expected, format_err_msg(expected, result)


@run_test
def find_wrong_way_fruit_should_find_intermediate_reversed_item():
    result = find_wrong_way_fruit(["banana", "ananab", "banana", "banana"])
    expected = 1
    assert result == expected, format_err_msg(expected, result)


"""
This function takes a string of DNA, such as 'GTCA', and returns a list
containing correctly matched DNA pairs.

The pairs are as follows:

'G' -> 'C'
'C' -> 'G'
'T' -> 'A'
'A' -> 'T'

The function should ignore any letters that are not valid DNA pairs
(e.g. not 'G', 'C', 'T' or 'A').
However, it should also work for lowercase and uppercase letters.

dna_pairs('G') # returns ['GC']
dna_pairs('GAT') # returns ['GC', 'AT', 'TA']
dna_pairs('GYTC') # returns ['GC', 'TA', 'CG']
dna_pairs('gat') # returns ['GC', 'AT', 'TA']

"""


def dna_pairs(dna_string):

    dna_upper = dna_string.upper()
    result =[]
    for char in list(dna_upper):
        match char:
            case 'G':
                result.append("GC")
            case 'C':
                result.append("CG")
            case 'A':
                result.append("AT")
            case 'T':
                result.append("TA")
    return result
            

    pass


@run_test
def dna_pairs_should_return_empty_list_for_empty_string():
    result = dna_pairs("")
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_empty_list_for_single_invalid_letter():
    result = dna_pairs("B")
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_uppercase_letter_G():
    result = dna_pairs("G")
    expected = ["GC"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_uppercase_letter_C():
    result = dna_pairs("C")
    expected = ["CG"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_uppercase_letter_T():
    result = dna_pairs("T")
    expected = ["TA"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_uppercase_letter_A():
    result = dna_pairs("A")
    expected = ["AT"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_lowercase_letter_g():
    result = dna_pairs("g")
    expected = ["GC"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_lowercase_letter_c():
    result = dna_pairs("c")
    expected = ["CG"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_lowercase_letter_t():
    result = dna_pairs("t")
    expected = ["TA"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_single_valid_lowercase_letter_a():
    result = dna_pairs("a")
    expected = ["AT"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_valid_list_for_long_valid_uppercase_string():
    result = dna_pairs("GAT")
    expected = ["GC", "AT", "TA"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_valid_list_for_long_uppercase_string_with_invalid_chars():
    result = dna_pairs("GYTC")
    expected = ["GC", "TA", "CG"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def dna_pairs_should_return_valid_list_for_mixed_string():
    result = dna_pairs("CGauTzgAcj")
    expected = ["CG", "GC", "AT", "TA", "GC", "AT", "CG"]
    assert result == expected, format_err_msg(expected, result)


"""
This function receives a `tweet` that will contain a number of mentions and
hashtags as on Twitter, sorry 'X'.
A hashtag is marked by `#` and a mention is marked by `@`.

The function should return a dictionary describing the number of hashtags and
mentions found in the string:
Example:
tweet = "So excited to start at @northcoders on Monday!
#learntocode #codingbootcamp"

tally_hashtags_and_mentions(tweet) # returns {'hashtags': 2, 'mentions': 1}
"""


def tally_hashtags_and_mentions(tweet):

    return{'hashtags':tweet.count("#"),'mentions': tweet.count("@")}
    pass


@run_test
def tally_hashtags_and_mentions_should_return_0_for_empty_tweet():
    result = tally_hashtags_and_mentions("")
    expected = {"hashtags": 0, "mentions": 0}
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_hashtags_and_mentions_should_return_1_for_single_hashtag():
    result = tally_hashtags_and_mentions("#omg")
    expected = {"hashtags": 1, "mentions": 0}
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_hashtags_and_mentions_should_return_1_for_single_mention():
    result = tally_hashtags_and_mentions("@paul_c")
    expected = {"hashtags": 0, "mentions": 1}
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_hashtags_and_mentions_should_return_1_for_tweet_containing_single_hashtag():
    result = tally_hashtags_and_mentions("Best place to learn #python?")
    expected = {"hashtags": 1, "mentions": 0}
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_hashtags_and_mentions_should_return_1_for_tweet_containing_single_mention():
    result = tally_hashtags_and_mentions("Need coding help, paging @Danika ...")
    expected = {"hashtags": 0, "mentions": 1}
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_hashtags_and_mentions_should_return_several_hashtags_and_mentions():
    result = tally_hashtags_and_mentions(
        "So excited to start at @northcoders on Monday! #learntocode #codingbootcamp"
    )
    expected = {"hashtags": 2, "mentions": 1}
    assert result == expected, format_err_msg(expected, result)


@run_test
def tally_hashtags_and_mentions_should_return_several_hashtags_and_mentions_mixed():
    result = tally_hashtags_and_mentions(
        "Thanks to @Alex and @Cat for helping with my #python #coding"
    )
    expected = {"hashtags": 2, "mentions": 2}
    assert result == expected, format_err_msg(expected, result)


if __name__ == "__main__":
    test_empty_string_invalid()
    test_length_less_than_eleven_is_invalid()
    test_length_more_than_fourteen_invalid()
    test_valid_examples_length_eleven()
    test_invalid_examples_length_eleven()
    test_length_twelve_invalid()
    test_valid_examples_length_thirteen()
    test_invalid_examples_length_thirteen()
    test_valid_examples_length_fourteen()
    test_invalid_examples_length_fourteen()
    test_invalid_if_contains_non_numeric_characters_other_than_first()

    sum_digits_from_string_should_return_0_for_empty_string()
    sum_digits_from_string_should_return_0_for_non_numeric_string()
    sum_digits_from_string_should_return_integer_for_single_digit()
    sum_digits_from_string_should_return_sum_for_two_digits()
    sum_digits_from_string_should_return_sum_for_three_digits()
    sum_digits_from_string_should_return_sum_for_mixed_string()
    sum_digits_from_string_should_return_0_for_no_numbers()

    get_williams_should_return_empty_list_for_empty_list()
    get_williams_should_return_empty_list_for_single_invalid_item()
    get_williams_should_return_single_valid_item()
    get_williams_should_return_several_valid_items()
    get_williams_should_return_mixed_items()
    get_williams_should_return_empty_list_for_mixed_items_with_rogue_williams()

    get_factorials_should_return_empty_list_for_empty_list()
    get_factorials_should_return_single_item()
    get_factorials_should_return_multiple_items()
    get_factorials_should_return_factorial_of_1()

    largest_number_should_return_single_digit()
    largest_number_should_return_double_digits_in_correct_order()
    largest_number_should_return_double_digits_in_incorrect_order()
    largest_number_should_return_double_digits_repeated()
    largest_number_should_return_triple_digits_in_correct_order()
    largest_number_should_return_triple_digits_in_incorrect_order()
    largest_number_should_return_triple_digits_with_two_repeated()
    largest_number_should_return_lots_of_digits()

    generate_matrix_should_return_empty_list_for_zero()
    generate_matrix_should_return_single_nested_list_for_single_digit()
    generate_matrix_should_return_two_nested_lists_for_two_digits()
    generate_matrix_should_return_three_nested_lists_for_three_digits()

    find_wrong_way_fruit_should_return_zero_for_singleton_list()
    find_wrong_way_fruit_should_return_zero_for_list_length_two()
    find_wrong_way_fruit_should_find_last_item_if_reversed()
    find_wrong_way_fruit_should_find_first_item_if_reversed()
    find_wrong_way_fruit_should_find_intermediate_reversed_item()

    dna_pairs_should_return_empty_list_for_empty_string()
    dna_pairs_should_return_empty_list_for_single_invalid_letter()
    dna_pairs_should_return_single_valid_uppercase_letter_G()
    dna_pairs_should_return_single_valid_uppercase_letter_C()
    dna_pairs_should_return_single_valid_uppercase_letter_T()
    dna_pairs_should_return_single_valid_uppercase_letter_A()
    dna_pairs_should_return_single_valid_lowercase_letter_g()
    dna_pairs_should_return_single_valid_lowercase_letter_c()
    dna_pairs_should_return_single_valid_lowercase_letter_t()
    dna_pairs_should_return_single_valid_lowercase_letter_a()
    dna_pairs_should_return_valid_list_for_long_valid_uppercase_string()
    dna_pairs_should_return_valid_list_for_long_uppercase_string_with_invalid_chars()
    dna_pairs_should_return_valid_list_for_mixed_string()

    tally_hashtags_and_mentions_should_return_0_for_empty_tweet()
    tally_hashtags_and_mentions_should_return_1_for_single_hashtag()
    tally_hashtags_and_mentions_should_return_1_for_single_mention()
    tally_hashtags_and_mentions_should_return_1_for_tweet_containing_single_hashtag()
    tally_hashtags_and_mentions_should_return_1_for_tweet_containing_single_mention()
    tally_hashtags_and_mentions_should_return_several_hashtags_and_mentions()
    tally_hashtags_and_mentions_should_return_several_hashtags_and_mentions_mixed()
