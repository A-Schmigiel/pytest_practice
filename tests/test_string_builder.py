from lib.string_builder import *

def test_string_builder():
    new_string = StringBuilder()
    new_string.add("Here's a new str")
    new_string.add("ing!")
    size = new_string.size()
    output = new_string.output()
    assert size == 20 and output == "Here's a new string!"