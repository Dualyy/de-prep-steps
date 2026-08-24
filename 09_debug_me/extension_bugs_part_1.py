import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg
# DO NOT CHANGE CODE ABOVE THIS LINE

# Fix the function below to pass the tests!

def confused_greeting(names):

    confused_shouts = []

    for name in names:
        confused_shouts.append(name + "?!")

    return confused_shouts


@run_test
def test_returns_empty_list_when_passed_empty_list():
    expected = []
    result = confused_greeting([])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_list_with_one_name_appended_with_symbols():
    expected = ['Alex?!']
    result = confused_greeting(["Alex"])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_list_of_names_with_symbols_appended():
    expected = ['Joe?!', 'Paul?!', 'Chon?!', 'Kyle?!']
    result = confused_greeting(['Joe', 'Paul', 'Chon', 'Kyle'])
    assert result == expected, format_err_msg(expected, result)



# Fix the function below to pass the tests!

def clever_banking(value, interest_rate, years):

    bank_account = value

    if interest_rate == 0:
        return value
    if years == 0 :
        return value
    
    for i in range(1, years + 1):
        bank_account *= (1 + interest_rate)
    
    return round(bank_account,2)


@run_test
def test_returns_same_value_when_interest_is_zero_for_5_years():
    expected = 100
    result = clever_banking(100, 0, 5)
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_same_value_when_years_are_0():
    expected = 100
    result = clever_banking(100, 3.2, 0)
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_correct_when_interest_rates_and_years_are_greater_than_0():
    expected = 161.05
    result = clever_banking(100, 0.1, 5)
    assert result == expected, format_err_msg(expected, result)


# Fix the function below to pass the tests!

def capital_authors(list):
    authors = []

    for pair in list:
        authors.append(pair.split()[0].upper().strip(" "))

    return authors


@run_test
def test_returns_an_empty_list_when_passed_one():
    expected = []
    result = capital_authors([])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_a_list_with_one_author_capitalised():
    expected = ["DANIKA"]
    result = capital_authors(["Danika - BASH your way out of any problem"])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_list_of_capitalised_authors():
    expected = ['JOE', "PAUL", "SIMON"]
    result = capital_authors([
        "Joe - Data: Now I own you",
        "Paul - How I become a god",
        "Simon - Why rocks are wicked super cool"
    ])
    assert result == expected, format_err_msg(expected, result)


# Fix the function below to pass the tests!

def sum_sentence(list):
    costs = []
    for fruit_dict in list:
        costs.append(fruit_dict['cost'])

    total = sum(costs)

    return "The total cost of the fruits is £" + str(total)


@run_test
def test_returns_correct_string_when_passed_an_empty_list():
    expected = "The total cost of the fruits is £0"
    result = sum_sentence([])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_correct_string_for_one_fruit():
    expected = "The total cost of the fruits is £5"
    result = sum_sentence([{"fruit": "apple", "cost": 5}])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_correct_string_for_multiple_fruits():
    expected = "The total cost of the fruits is £33"
    result = sum_sentence([
        {"fruit": "red apple", "cost": 5},
        {"fruit": "poison apple", "cost": 20},
        {"fruit": "kiwi", "cost": 1},
        {"fruit": "tomato ;)", "cost": 2},
        {"fruit": "green apple", "cost": 5},
    ])
    assert result == expected, format_err_msg(expected, result)

if __name__ == '__main__':
    test_returns_empty_list_when_passed_empty_list()
    test_returns_list_with_one_name_appended_with_symbols()
    test_returns_list_of_names_with_symbols_appended()
    test_returns_same_value_when_interest_is_zero_for_5_years()
    test_returns_same_value_when_years_are_0()
    test_returns_correct_when_interest_rates_and_years_are_greater_than_0()
    test_returns_an_empty_list_when_passed_one()
    test_returns_a_list_with_one_author_capitalised()
    test_returns_list_of_capitalised_authors()
    test_returns_correct_string_when_passed_an_empty_list()
    test_returns_correct_string_for_one_fruit()
    test_returns_correct_string_for_multiple_fruits()