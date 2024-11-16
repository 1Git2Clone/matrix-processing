# ---------------------------
# Necessary path manipulation
# ---------------------------

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


# -------------
# Testing utils
# -------------


from utils.constants import (
    TEST_MATRIX_UPPER_TRIANG,
    TEST_MATRIX_LOWER_TRIANG,
    TEST_MATRIX_IDENTITY,
)

from utils.decorators import test


# -------------
# Project utils
# -------------

from src.utils.inv import rounded_matmul, get_inversed_matrix


@test(test_count=1, exec_args=[])
def proper_inversion_equality() -> None:
    """
    Running assertion tests to make sure all the inverse matrix calculations
    are calculated properly.
    """
    assert (
        rounded_matmul(TEST_MATRIX_UPPER_TRIANG).all()
        == get_inversed_matrix(TEST_MATRIX_UPPER_TRIANG).all()
    )
    assert (
        rounded_matmul(TEST_MATRIX_LOWER_TRIANG).all()
        == get_inversed_matrix(TEST_MATRIX_LOWER_TRIANG).all()
    )
    assert rounded_matmul(TEST_MATRIX_UPPER_TRIANG).all() == TEST_MATRIX_IDENTITY.all()
    assert rounded_matmul(TEST_MATRIX_LOWER_TRIANG).all() == TEST_MATRIX_IDENTITY.all()
