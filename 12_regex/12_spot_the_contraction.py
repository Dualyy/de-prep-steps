import os
import sys
import re

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def spot_the_contraction(text):
    """
    Write a function using regex to return True if a sentence contains any of
    these contractions: "I'm", "I've" or "don't". (case insensitive)

    This function will take a string and return True or False. See examples
    below:

    - "do not" False
    - "don't" True
    - "I am" False
    - I have been fishing and I've caught plenty fishes True
    - "I am a coding panda" False
    - "I'm a coding panda" True
    - I've got a collection of foreign coins True
    - "Sometimes I do not like to get up early" False
    - "Sometimes I don't like to get up early" True
    - "Don't feed the birds" True
    """

    regex = re.compile(r'\w+\'\w+')
    return True if regex.search(text) else False
                       
    pass


@run_test
def test_spot_the_contraction_returns_true_when_contraction_spotted():
    assert spot_the_contraction("I am a vampire and I don't drink water"), \
        format_err_msg(True, spot_the_contraction(
            "I am a vampire and I don't drink water"))
    assert spot_the_contraction("I've got a collection of foreign coins"), \
        format_err_msg(True, spot_the_contraction(
            "I've got a collection of foreign coins"))


@run_test
def test_spot_the_contraction_returns_false_when_contraction_not_spotted():
    assert not spot_the_contraction("do not"), \
        format_err_msg(False, spot_the_contraction("do not"))
    assert not spot_the_contraction("I am"), \
        format_err_msg(False, spot_the_contraction("I am"))
    assert not spot_the_contraction("I am a coding panda"), \
        format_err_msg(False, spot_the_contraction("I am a coding panda"))
    assert not spot_the_contraction("Sometimes I do not like to get up early"), \
        format_err_msg(
            False, spot_the_contraction("Sometimes I do not like to get up early"))
    assert not spot_the_contraction("I have been fishing"), \
        format_err_msg(False, spot_the_contraction("I have been fishing"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_spot_the_contraction_returns_true_when_contraction_spotted()
    test_spot_the_contraction_returns_false_when_contraction_not_spotted()
