from inspect import signature

from typing import Any, Callable


def print_fn_to_str(fn: Callable) -> str:
    fn_sig = signature(fn)
    return (
        f"def {fn.__name__}"
        + f"({"".join([f"{param_name}: {param.annotation.__name__}" for param_name, param in fn_sig.parameters.items()] or "")})"
        + f" -> {fn_sig.return_annotation or None}: ..."
    )


def print_fn(fn: Callable) -> None:
    print(print_fn_to_str(fn))


def print_args_to_str(args: list[Any]) -> str:
    formatted_args = ", ".join([f"{arg}: {type(arg).__name__}" for arg in args])
    return f"CURRENT ARGS ({len(args)}): [{formatted_args}]."


def print_args(args: list[Any]) -> None:
    print(print_args_to_str(args))
