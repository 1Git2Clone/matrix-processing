import numpy as np
from numpy.typing import NDArray

import scipy.linalg as linalg


def get_inversed_matrix(input: NDArray) -> NDArray:
    inversed = linalg.inv(input)
    inversed[inversed == -0.0] = 0.0
    return inversed


def rounded_matmul(input: NDArray, cmp: NDArray | None = None):
    """
    Gets input x cmp whilst replacing all -0.0 instances to 0.0 and rounding
    down the result to 10 decimal places (due to rounding imprecisions).

    NOTE:
        This is NOT the same as cmp x input UNLESS cmp is input^(-1)!

    Defaults:
        cmp = input^(-1).
    """
    if cmp is None:
        cmp = get_inversed_matrix(input)
    input_times_cmp = np.round(input @ cmp, 10)
    input_times_cmp[input_times_cmp == -0.0] = 0.0
    return input_times_cmp
