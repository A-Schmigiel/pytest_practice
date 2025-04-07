import pytest
import random
import string
from lib.check_codeword import check_codeword

# def test_check_codeword_horse():
#     assert check_codeword('horse') == 'Correct! Come in.'
    
# def test_check_codeword_random_close():
#     length = random.randint(1, 10)
#     random_but_close = 'h'+ str(''.join(random.choice(string.ascii_lowercase)) for i in range(length)) + 'e'
#     assert check_codeword(random_but_close) == 'Close, but nope.'

# def test_check_codeword_wrong():
#     anything_else = 
#     assert 

@pytest.mark.parametrize(
    'codeword, expected_result', 
    [
        ('horse', 'Correct! Come in.'),
        ('h' + (str(''.join(random.choice(string.ascii_lowercase)) for i in range(random.randint(1, 10))) + 'e'), 'Close, but nope.'),
        ('steve', 'WRONG!'),
        (str(random.choice(string.ascii_lowercase) and not 'h') + (str(''.join(random.choice(string.ascii_lowercase)) for i in range(random.randint(1, 10)))), 'WRONG!'),
        ((str(''.join(random.choice(string.ascii_lowercase)) for i in range(random.randint(1, 10)))) + (str(random.choice(string.ascii_lowercase) and not 'e')), 'WRONG!'),
        ('please?', 'WRONG!')
    ],
)

def test_check_codeword(codeword, expected_result):
    assert check_codeword(codeword) == expected_result 
