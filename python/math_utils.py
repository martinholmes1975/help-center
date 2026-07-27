# math_utils.py - Mathematical utility functions


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
