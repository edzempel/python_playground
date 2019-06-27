import inc_dec  # code to test


def test_increment():
    assert inc_dec.increment(1) == 2
    assert inc_dec.increment(-1) == 0
    assert inc_dec.increment(0) == 1


def test_decrement():
    assert inc_dec.decrement(1) == 0
    assert inc_dec.decrement(-1) == -2
    assert inc_dec.decrement(0) == -1
