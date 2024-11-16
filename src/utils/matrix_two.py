import numpy as np

from numpy._typing import NDArray
from .types import NullMatrix, Num


type Matrix2D = list[list[Num]]


def new_2d_matrix(width: int, height: int) -> Matrix2D:
    """
    Used to allocate memory for a 2D matrix (list[list[...]]) in order to be
    able to safely index it.
    """
    return [[0] * width for _ in range(height)]


def display_matrix(matrix: NDArray, header: str = "") -> None:
    """
    Displays the input matrix with a custom header (optional).

    NOTE:
        This implementation REQURES the matrix to not be an empty matrix!

    Possible exceptions:
        IndexError
    """
    print(
        "*" * len(header),
        f"{header}",
        "*" * len(header),
        f"{np.array2string(
            matrix,
            formatter={
                'float_kind': (
                    lambda x: f"{x:{len(matrix[0])}}"
                ),
            }
        )}",
        "*" * len(header),
        "-" * 80,
        sep="\n",
    )


def user_input_2d_matrix() -> Matrix2D | NullMatrix:
    i = str()
    while not isinstance(i, int):
        try:
            i = int(input("Enter matrix width: "))
            break
        except ValueError as e:
            print(e)

    j = input(f"Enter matrix height (Default: {i}): ")
    try:
        j = int(j)
    except ValueError:
        j = i

    if any([i, j]) == 0:
        return NullMatrix()

    arr: Matrix2D = new_2d_matrix(width=i, height=j)

    for row in range(i):
        for col in range(j):
            item = str()
            while not isinstance(item, float):
                try:
                    item = float(
                        input(f"Enter item for [row {row+1}], [col: {col+1}]: ")
                    )
                    break
                except ValueError as e:
                    print(e)

            arr[row][col] = item

    return arr
