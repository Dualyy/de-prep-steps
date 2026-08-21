import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, format_err_msg, skip_test
# DO NOT CHANGE CODE ABOVE THIS LINE

def remove_mark_down_headings(markdown_heading):
    """
    This function should accept a string containing a markdown heading and return the text content without the hash tags and preceding space.

    Markdown is a file format that is popular with developers. 
    Our README files are written in this format. 
    One way to define a heading in markdown is with between 1 and 6 #s.

    # This is the Title
    ## First Section
    ### A sub heading in section 1
    ## Second Section

    Research an appropriate string method to achieve this. 
    (There's one on this page that can do this https://docs.python.org/3/library/stdtypes.html#string-methods).
    
    """
    return markdown_heading.replace('#','').removeprefix(' ')
    pass


@run_test
def test_remove_single_mark_down_headings():
    assert remove_mark_down_headings("# Title") == "Title", \
        format_err_msg("Title", remove_mark_down_headings("# Title"))


@run_test
def test_remove_multiple_mark_down_headings():
    assert remove_mark_down_headings("## Sub Heading") == "Sub Heading", \
        format_err_msg(
            "Sub Heading", remove_mark_down_headings("## Sub Heading"))

    assert remove_mark_down_headings("### level 3") == "level 3", \
        format_err_msg(
            "level 3", remove_mark_down_headings("### level 3"))


if __name__ == '__main__':
    test_remove_single_mark_down_headings()
    test_remove_multiple_mark_down_headings()
