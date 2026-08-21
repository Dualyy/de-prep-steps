import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, format_err_msg, skip_test
# DO NOT CHANGE CODE ABOVE THIS LINE

def is_suspicious(crew_mates):
    """
    This function will find take a list of crew_mates and return a True when the list contains the string "imposter" and False if not.

    Use the built-in any function to find out if any of the crew_mates are the string imposter.

    Pay attention to the behaviour of any with its arguments - comprehensions may be useful here.
    """
    
    return any(["imposter" in crew_mates for crew_mate in crew_mates])

    pass


@run_test
def test_is_not_suspicious():
    assert is_suspicious([]) is False, \
        format_err_msg(False, is_suspicious([]))

    assert is_suspicious(["innocent northcoder"]) is False, \
        format_err_msg(False, is_suspicious(["innocent northcoder"]))

    test_group = ["renegade northcoder",
                  "imposing northcoder", "hard working northcoder"]
    assert is_suspicious(test_group) is False, \
        format_err_msg(False, is_suspicious(test_group))


@run_test
def test_is_suspicious():
    assert is_suspicious(["imposter"]) is True, \
        format_err_msg(True, is_suspicious(["imposter"]))

    test_group = ["northcoder happily doing their tasks",
                  "suspicious northcoder", "imposter"]
    assert is_suspicious(test_group) is True, \
        format_err_msg(True, is_suspicious(test_group))


if __name__ == '__main__':
    test_is_not_suspicious()
    test_is_suspicious()