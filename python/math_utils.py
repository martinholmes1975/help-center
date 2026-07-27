# math_utils.py - Mathematical and statistical utility functions


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


def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def is_even(n: int) -> bool:
    """Checks if an integer is even."""
    return n % 2 == 0


def factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
