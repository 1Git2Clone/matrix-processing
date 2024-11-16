from typing import Callable, Any

from textwrap import wrap

from tests.utils.constants import FORMAT_CENTER
from tests.utils.printing import print_args_to_str, print_fn, print_fn_to_str


def test(test_count: int, exec_args: list[Any] = []) -> Callable:
    """
    I could do `@lambda _: ()` as a decorator instead but that's unreadable...
    """

    def inner(fn: Callable) -> None:
        print("-" * 80)
        print(f"RUNNING TEST: #{test_count}".center(80))
        print("-" * 80)

        print_fn(fn)
        if fn.__doc__ is not None:
            print("DOCSTRING:")
            print(f"{fn.__doc__}".center(FORMAT_CENTER))

        print("*** RESULT ***".center(FORMAT_CENTER))

        print("-" * FORMAT_CENTER)
        try:
            print("TEST OUTPUT:")
            fn(*exec_args)
            print("SUCCESS!".center(FORMAT_CENTER))
        except AssertionError as e:
            print("ASSERTION ERROR!".center(FORMAT_CENTER))
            print(e)
            raise e
        except TypeError as e:
            print("TYPE ERROR!".center(FORMAT_CENTER))
            print(e)
            print(end="\n")
            print(
                "\n".join(
                    wrap(
                        "**HINT**: Make sure to double check the decorator's `exec_args` "
                        + "property and make the count (and position) of the "
                        + f"arguments the same as your function ({fn.__name__}). "
                    ),
                )
                + "\n"
                + print_args_to_str(exec_args),
            )
            print(end="\n")
            raise e
        except Exception as e:
            print("EXCEPTION!".center(FORMAT_CENTER))
            print(e)
            raise e
        finally:
            print(
                "".join(
                    "(on " + print_fn_to_str(fn) + f" | TEST #{test_count})"
                ).center(80)
            )
            print("-" * 80)

    return inner
