# math_utils.py - Statistical utility functions


def mean(numbers: list[float]) -> float:
    """Calculates the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list.")
    return sum(numbers) / len(numbers)


def maximum(numbers: list[float]) -> float:
    """Returns the maximum value in a list of numbers."""
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    return max(numbers)


def minimum(numbers: list[float]) -> float:
    """Returns the minimum value in a list of numbers."""
    if not numbers:
        raise ValueError("Cannot find the minimum of an empty list.")
    return min(numbers)


def range_of(numbers: list[float]) -> float:
    """Calculates the difference between the maximum and minimum values."""
    if not numbers:
        raise ValueError("Cannot calculate the range of an empty list.")
    return max(numbers) - min(numbers)
