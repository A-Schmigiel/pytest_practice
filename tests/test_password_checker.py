from lib.password_checker import *
import pytest

def test_check_error():
    error_pass_check = PasswordChecker()
    with pytest.raises(Exception) as e:
        error_pass_check.check('1234567')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'

def test_check():
    new_pass_check = PasswordChecker()
    result = new_pass_check.check('123456789')
    assert result == True