from inspect import signature

from typing import Callable


def print_fn_to_str(fn: Callable) -> str:
    fn_sig = signature(fn)
    return (
        f"def {fn.__name__}"
        + f"({"".join([f"{param_name}: {param.annotation.__name__}" for param_name, param in fn_sig.parameters.items()] or "")})"
        + f" -> {fn_sig.return_annotation or None}: ..."
    )


def print_fn(fn: Callable) -> None:
    print(print_fn_to_str(fn))
