from lib.present import *
import pytest

# test that each function works

def test_present():
    new_present = Present()
    new_present.wrap('an avacado!')
    new_present.unwrap()

def test_present_exception_wrap():
    wrapped_present = Present()
    wrapped_present.wrap('little egg')
    with pytest.raises(Exception) as e:
        wrapped_present.wrap('a brand new car') #should throw exception
    error_message = str(e.value)
    assert error_message == "A little egg has already been wrapped."

def test_present_exception_unwrap():
    empty_present = Present()
    with pytest.raises(Exception) as e:
        empty_present.unwrap()
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'