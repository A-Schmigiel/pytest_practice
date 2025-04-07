import random
import string
from lib.report_length import report_length

def test_report_length():
    str1 = (str(''.join(random.choice(string.ascii_lowercase)) for i in range(random.randint(1, 1000))))
    len1 = len(str1)
    assert report_length(str1) == f"This string was {len1} characters long."
