"""A decorator that validates division input."""
# The decorator runs validation before the decorated `divide` function.
from functools import wraps


def require_larger_denominator(function):
    @wraps(function)
    def wrapper(numerator: float, denominator: float) -> float:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator <= numerator:
            raise ValueError("Denominator must be greater than numerator.")
        return function(numerator, denominator)

    return wrapper


@require_larger_denominator
def divide(numerator: float, denominator: float) -> float:
    return numerator / denominator


if __name__ == "__main__":
    print(divide(5, 10))
