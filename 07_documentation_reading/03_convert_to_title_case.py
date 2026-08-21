import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, format_err_msg, skip_test
# DO NOT CHANGE CODE ABOVE THIS LINE

def convert_to_title_case(sentence):
    """
    This function will take a string and uppercase the first letter of each word. In Python, strings come with a .title() method that almost serves our purposes.

    It does, however, suffer from a problem in the way it defines words.

    "they're bill's friends from the UK".title() - Returns: "They'Re Bill'S Friends From The Uk"
    
    Your function should account for this and not treat them as separate words. The documentation contains some proposed workarounds for this. 
    https://docs.python.org/3/library/stdtypes.html#str.title
    
    Use their suggestions to complete your function.
    """
    import string
    formatted = string.capwords(sentence)

    return formatted
    pass


@run_test
def test_convert_single_word_to_title_case():
    assert convert_to_title_case("hi") == "Hi", \
        format_err_msg("Hi", convert_to_title_case("hi"))


@run_test
def test_convert_multi_word_to_title_case():
    assert convert_to_title_case("hello world") == "Hello World", \
        format_err_msg("Hello World", convert_to_title_case("hello world"))

    assert convert_to_title_case("Goodbye world") == "Goodbye World", \
        format_err_msg("Goodbye World", convert_to_title_case("Goodbye world"))

    assert convert_to_title_case("Well ain't this awkward") == \
        "Well Ain't This Awkward", \
        format_err_msg("Well Ain't This Awkward",
                       convert_to_title_case("Well ain't this awkward"))


@run_test
def test_convert_complex_sentence_to_title_case():
    assert convert_to_title_case(
        "not just apostrophes, could be something-else") \
        == "Not Just Apostrophes, Could Be Something-else", \
        format_err_msg(
            "Not Just Apostrophes, Could Be Something-else",
            convert_to_title_case(
                "not just apostrophes, could be something-else"))


if __name__ == '__main__':
    test_convert_single_word_to_title_case()
    test_convert_multi_word_to_title_case()
    test_convert_complex_sentence_to_title_case()