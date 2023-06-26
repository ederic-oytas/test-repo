import numpy as np

from test_oyster.adding import add, sum_1d_array


def test_add():
    assert add(1, 2) == 3
    assert add(20, 25) == 45
    assert add(1000, 2500) == 3500


def test_sum_1d_array():
    assert test_sum_1d_array(np.array([1, 2, 3])) == 6.0
    assert test_sum_1d_array(np.array([10.0])) == 6.0
    assert test_sum_1d_array(np.array([5.0, 3.5])) == 8.5
