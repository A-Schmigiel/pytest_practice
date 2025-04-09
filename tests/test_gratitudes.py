from lib.gratitudes import *
import pytest

def test_gratitude():
    new_thanks = Gratitudes()
    new_thanks.add('pizza')
    new_thanks.add('puppies')
    new_thanks.add('pirates')
    assert new_thanks.format() == "Be grateful for: pizza, puppies, pirates"#

def test_format_empty():
    no_thanks = Gratitudes()
    assert no_thanks.format() == "Be grateful for: "

def test_one_thing():
    one_thank = Gratitudes()
    one_thank.add('puppies')
    assert one_thank.format() == "Be grateful for: puppies"