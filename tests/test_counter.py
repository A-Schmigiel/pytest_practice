import random
from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(25)
    counter.add(0)
    counter.add(1)
    result = counter.report()
    assert result == f"Counted to 26 so far."

def test_counter_rand():
    counter_rand = Counter()
    rand_num = random.randint(0, 999)
    counter_rand.add(rand_num)
    counter_rand.add(0)
    result = counter_rand.report()
    assert result == f"Counted to {rand_num} so far."
