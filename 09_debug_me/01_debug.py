import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg
# DO NOT CHANGE CODE ABOVE THIS LINE

#  Fix the function below to pass the test!

def say_hello():
    return "Hello Data Engineers."


@run_test
def test_returns_correct_value():
    expected = 'Hello Data Engineers.'
    result = say_hello()
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_correct_value()