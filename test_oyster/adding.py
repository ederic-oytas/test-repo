import numpy as np


def add(a: int, b: int) -> int:
    """Adds two integers together.

    Args:
        a: First argument.
        b: Second argument.

    Returns:
        The sum of the two integers.
    """
    return a + b


def sum_1d_array(a: np.ndarray) -> float:
    """Returns the sum of the given 1-dimensional array.

    Args:
        a: 1-dimensional array of real numbers.

    Returns:
        The sum of the 1D array.
    """
    total = 0.0
    for i in range(a.shape[0]):
        total += a[i]
    return total
