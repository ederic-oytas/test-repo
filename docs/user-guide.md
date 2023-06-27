
# User Guide

## The `add` Function

You can use `add` to add two integers together:

```python3
from test_oyster import add


assert add(3, 4) == 7
```

## The `sum_1d_array` function

You can use `sum_1d_array` to sum up a 1-dimensional array of real numbers.

```python
import numpy as np
from test_oyster import sum_1d_array


assert sum_1d_array(np.array([0, 2, 3])) == 5
```

## All done!

See our API [reference](reference.md) for info on each function.
