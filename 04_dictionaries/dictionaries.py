import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE
"""
### add_price_to_product ###

Write a function that takes a dictionary (`product`) that looks like this:
`{ 'type': 'Tofu slices' }`,
and a number (`price`). Add a price property to this dictionary and set its
value to the `price`.
Then, return the dictionary.

e.g.

add_price_to_product({ 'type': 'Tofu slices' }, 2.20) # returns
{ 'type': 'Tofu slices', 'price': 2.20 }
"""


def add_price_to_product(product, price):
    # Your code here
    if len(product) > 0:
        product['price'] = price
    return product
    pass


@run_test
def add_price_to_product_should_return_empty_dict_when_passed_an_empty_dict():
    updated_product = add_price_to_product({}, 2.20)
    expected = {}
    assert updated_product == expected, format_err_msg(expected, updated_product)


@run_test
def add_price_to_product_should_update_product_with_single_key():
    updated_product = add_price_to_product({"type": "Tofu slices"}, 2.20)
    expected = {"type": "Tofu slices", "price": 2.20}
    assert updated_product == expected, format_err_msg(expected, updated_product)


@run_test
def add_price_to_product_should_update_multi_field_product():
    updated_product = add_price_to_product(
        {"type": "Tofu slices", "flavour": "chocolate"}, 2.50
    )
    expected = {"type": "Tofu slices", "flavour": "chocolate", "price": 2.50}
    assert updated_product == expected, format_err_msg(expected, updated_product)


@run_test
def add_price_to_product_should_modify_original():
    product = {"type": "Tofu slices"}
    updated_product = add_price_to_product(product, 2.20)
    assert updated_product is product, format_err_msg(
        "original dictionary to be updated", "new dictionary"
    )


"""
### add_property_to_product ###

Write a function that takes three arguments:

 - a dictionary (`product`) that looks like this: `{'type': 'Terminator 2:
 Judgement Day', 'price': '£6.99', 'quantity': 1 }`
 - a `key` to add
 - a `value` corresponding to the key

It should then update the `product` to include this new attribute and return
the updated `product`.

add_attribute_to_product(
    {'type': 'Terminator 2: Judgement Day', 'price': '£6.99', 'quantity': 1 },
    'length', '2h 36m'
    )
#returns {
    # 'type': 'Terminator 2: Judgement Day',
    # 'price': '£6.99',
    # 'quantity': 1,
    # 'length': '2h 36m'
    # }

NOTE: Only certain types of data are able to be set a dictionary key. Your
function should take this into consideration and only allow the following data
types to be set as a key:
- string
- integer
- float
- boolean

If the given `key` argument is not one of these types then it should be
ignored and the product returned unchanged!
"""


def add_attribute_to_product(product, key, value):
    # Your code here
    if type(key) not in (str,int,float,bool):
        return product
    product[key] = value

    return product
    pass


# ❗ Remember to change @skip_test to @run_test!
@run_test
def add_attribute_to_product_should_add_single_attribute_to_empty_product():
    result = add_attribute_to_product({}, "length", "2h 36m")
    expected = {"length": "2h 36m"}
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_add_string_attribute_to_product():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, "length", "2h 36m")
    expected = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        "length": "2h 36m",
    }
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_add_integer_attribute_to_product():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, 36, 42)
    expected = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        36: 42,
    }
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_add_float_attribute_to_product():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, 36.1, "dave")
    expected = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        36.1: "dave",
    }
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_add_boolean_attribute_to_product():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, True, False)
    expected = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        True: False,
    }
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_not_add_list_attribute_to_product():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, [1, 2, 3], "a")
    expected = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_not_add_dictionary_attribute_to_product():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, {"a": "b"}, "a")
    expected = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    assert result == expected, format_err_msg(expected, result)


@run_test
def add_attribute_to_product_should_return_the_original_product_dictionary():
    product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
    result = add_attribute_to_product(product, "length", "2h 36m")
    assert result is product, format_err_msg(
        "original input dictionary", "new dictionary"
    )


"""
### create_northcoder ###

Write a function that takes a string (name) and a number (year_of_birth) and
returns a dictionary with:

 - a name property set to the value of the name parameter
 - an age property set to whatever the age of the northcoder would be in the
 year 2023
 - a language property set to 'Python'

If the year is after 2023, show 'error' for the age.

create_northcoder('Joe', 2002)

returns
{
  'name': 'Joe',
  'age': 21,
  'language': 'Python'
}
"""


def create_northcoder(name, year_of_birth):
    northcoder = {}
    northcoder['name'] = name
    if year_of_birth > 2023:
        northcoder['age'] = 'error'
    else:
        northcoder["age"] = 2023 - year_of_birth

    northcoder['language'] = 'Python'
    return northcoder
    pass


@run_test
def create_northcoder_should_create_northcoder_with_correct_age():
    result = create_northcoder("Joe", 2002)

    expected = {"name": "Joe", "age": 21, "language": "Python"}

    assert result == expected, format_err_msg(expected, result)


@run_test
def create_northcoder_should_add_age_as_0_for_birth_year_2023():
    result = create_northcoder("Paul", 2023)
    expected = {"name": "Paul", "age": 0, "language": "Python"}
    assert result == expected, format_err_msg(expected, result)


@run_test
def create_northcoder_should_show_age_error_if_birth_year_is_after_2023():
    result = create_northcoder("Zarkon", 2123)
    expected = {"name": "Zarkon", "age": "error", "language": "Python"}
    assert result == expected, format_err_msg(expected, result)


"""
### delete_many_passwords ###

Write a function that takes an array of user dictionaries (`users`), and
deletes the password key value pair on each user and returns the list.
If a dictionary does not already have a password key then it should be
unchanged.

delete_many_passwords([
    {'name': 'Barry', 'password': 'ilovetea', 'department': 'Tea'},
    {
        'name': 'Sandeep',
        'password': 'ilovecoffee',
        'favourite_drink': 'Coffee'
        },
    {'name': 'Kavita', 'password': 'ilovepie', 'weakness': 'Pie'}
])

Returns
[
    { 'name': 'Barry', 'department': 'Tea'},
    { 'name': 'Sandeep', 'favourite_drink': 'Coffee' },
    { 'name': 'Kavita', 'weakness': 'Pie'}
]
"""


def delete_many_passwords(users):
    for user in users:
        if 'password' in user.keys():
            user.pop('password')
    return users
    pass


@run_test
def delete_many_passwords_should_change_single_password():
    result = delete_many_passwords(
        [{"name": "Barry", "password": "ilovetea", "department": "Tea"}]
    )
    expected = [{"name": "Barry", "department": "Tea"}]
    assert result == expected, format_err_msg(expected, result)


@run_test
def delete_many_passwords_should_not_change_user_without_password():
    result = delete_many_passwords([{"name": "Sandeep", "favourite_drink": "Coffee"}])
    expected = [{"name": "Sandeep", "favourite_drink": "Coffee"}]
    assert result == expected, format_err_msg(expected, result)


@run_test
def delete_many_passwords_should_change_many_users():
    result = delete_many_passwords(
        [
            {"name": "Barry", "password": "ilovetea", "department": "Tea"},
            {"name": "Sandeep", "password": "ilovecoffee", "favourite_drink": "Coffee"},
            {"name": "Kavita", "password": "ilovepie", "weakness": "Pie"},
        ]
    )
    expected = [
        {"name": "Barry", "department": "Tea"},
        {"name": "Sandeep", "favourite_drink": "Coffee"},
        {"name": "Kavita", "weakness": "Pie"},
    ]
    assert result == expected, format_err_msg(expected, result)


@run_test
def delete_many_passwords_should_change_many_users_when_some_do_not_have_passwords():
    result = delete_many_passwords(
        [
            {"name": "Barry", "password": "ilovetea", "department": "Tea"},
            {"name": "Sandeep", "password": "ilovecoffee", "favourite_drink": "Coffee"},
            {"name": "Kavita", "weakness": "Pie"},
        ]
    )
    expected = [
        {"name": "Barry", "department": "Tea"},
        {"name": "Sandeep", "favourite_drink": "Coffee"},
        {"name": "Kavita", "weakness": "Pie"},
    ]
    assert result == expected, format_err_msg(expected, result)


@run_test
def delete_many_passwords_should_return_empty_list_when_no_users_present():
    result = delete_many_passwords([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


"""
### get_northcoders_names ###

Write a function that takes a list of dictionaries with the format from
create_northcoder (`northcoders`), and returns a new list of the users' names
as strings.
Any northcoders who are missing names should be omitted from the returned list.

northcoders = [
  {
    'name': 'Callum',
    'age': 31,
    'language': 'JavaScript'
  },
  {
    'name': 'Carrie',
    'age': 32,
    'language': 'Python'
  }
]

get_northcoders_names(northcoders) # returns ['Callum', 'Carrie']
"""


def get_northcoders_names(northcoders):
    names_of_northcoders = []
    for northcoder in northcoders:
        if northcoder.get('name'):
            names_of_northcoders.append(northcoder.get('name'))
    return names_of_northcoders
    pass


@run_test
def get_northcoders_names_should_return_empty_list_if_input_is_empty():
    result = get_northcoders_names([])
    expected = []
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_northcoders_names_should_get_names_of_northcoders():
    result = get_northcoders_names(
        [
            {"name": "Callum", "age": 31, "language": "JavaScript"},
            {"name": "Carrie", "age": 32, "language": "Python"},
        ]
    )
    expected = ["Callum", "Carrie"]
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_northcoders_names_should_ignore_northcoders_without_names():
    result = get_northcoders_names([{"age": 32, "language": "Python"}])
    expected = []
    assert result == expected, format_err_msg(expected, result)


"""
### get_user_pet_age ###

Write a function that takes a `user` dictionary that looks like this:

{
  'name': "Tom",
  'age': 26,
  'pet': {
    'name': "Barney",
    'age': 6,
    'type': "good boy"
  }
}

The dictionary is nested; there are dictionaries paired to keys on the user
dictionary.

The function should access the age property in the nested pet dictionary
and return the value.
If the user doesn't have an age for their pet the function should return None.

user = {
  'name': "Carrie",
  'age': 26,
  'pet': {
    'name': "Pixie",
    'age': 4,
    'type': "gremlin"
  }
}

get_user_pet_age(user) # returns 4
"""


def get_user_pet_age(user):
    if user.get('pet'):
        return user['pet'].get('age')
    else: return None
    pass


@run_test
def get_user_pet_age_should_return_pet_age():
    result = get_user_pet_age(
        {
            "name": "Carrie",
            "age": 26,
            "pet": {"name": "Pixie", "age": 4, "type": "gremlin"},
        }
    )
    expected = 4
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_user_pet_age_should_return_none_if_no_pet():
    result = get_user_pet_age({"name": "Carrie", "age": 26})
    expected = None
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_user_pet_age_should_return_none_if_no_pet_age():
    result = get_user_pet_age(
        {
            "name": "Carrie",
            "age": 26,
            "pet": {"name": "Pixie", "type": "gremlin"},
        }
    )
    expected = None
    assert result == expected, format_err_msg(expected, result)


if __name__ == "__main__":
    add_price_to_product_should_return_empty_dict_when_passed_an_empty_dict()
    add_price_to_product_should_update_product_with_single_key()
    add_price_to_product_should_update_multi_field_product()
    add_price_to_product_should_modify_original()
    add_attribute_to_product_should_add_single_attribute_to_empty_product()
    add_attribute_to_product_should_add_string_attribute_to_product()
    add_attribute_to_product_should_add_integer_attribute_to_product()
    add_attribute_to_product_should_add_float_attribute_to_product()
    add_attribute_to_product_should_add_boolean_attribute_to_product()
    add_attribute_to_product_should_not_add_list_attribute_to_product()
    add_attribute_to_product_should_not_add_dictionary_attribute_to_product()
    add_attribute_to_product_should_return_the_original_product_dictionary()
    create_northcoder_should_create_northcoder_with_correct_age()
    create_northcoder_should_add_age_as_0_for_birth_year_2023()
    create_northcoder_should_show_age_error_if_birth_year_is_after_2023()
    delete_many_passwords_should_change_single_password()
    delete_many_passwords_should_not_change_user_without_password()
    delete_many_passwords_should_change_many_users()
    delete_many_passwords_should_change_many_users_when_some_do_not_have_passwords()
    delete_many_passwords_should_return_empty_list_when_no_users_present()
    get_northcoders_names_should_return_empty_list_if_input_is_empty()
    get_northcoders_names_should_get_names_of_northcoders()
    get_northcoders_names_should_ignore_northcoders_without_names()
    get_user_pet_age_should_return_pet_age()
    get_user_pet_age_should_return_none_if_no_pet()
    get_user_pet_age_should_return_none_if_no_pet_age()
