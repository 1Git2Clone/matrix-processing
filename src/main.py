# ----------------------
# External library utils
# ----------------------

import numpy as np
import scipy.linalg as linalg

from numpy.typing import NDArray

# -------------
# Project utils
# -------------

from utils.types import NullMatrix

from utils.inv import get_inversed_matrix, rounded_matmul
from utils.matrix_two import (
    display_matrix,
    user_input_2d_matrix,
)


def do_matrix_calculations(input: NDArray):
    display_matrix(input, "User input matrix")
    try:
        inversed = get_inversed_matrix(input)
        display_matrix(inversed, "Inverse matrix")
        assert (
            rounded_matmul(input, inversed).all()
            == rounded_matmul(inversed, input).all()
        )
    except linalg.LinAlgError as e:
        print(f"scipy.linalg.LinAlgError: {e}")


def main():
    user_matrix = np.array(user_input_2d_matrix())
    if not isinstance(user_matrix, NullMatrix):
        do_matrix_calculations(user_matrix)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("System Interrupt.")
    except EOFError:
        print("System Interrupt.")
    finally:
        print("Exiting...")
