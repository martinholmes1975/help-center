# simple_utils.py - A utility library


def reverse_string(text: str) -> str:
    """Reverses the characters in a string."""
    return text[::-1]


def count_words(sentence: str) -> int:
    """Returns the word count of a given sentence."""
    return len(sentence.split())


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def calculate_average(numbers: list[float]) -> float:
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def parse_user_input(data: str) -> dict:
    """Parses a CSV string into a user dictionary."""
    parts = [p.strip() for p in data.split(",")]
    return {"name": parts[0], "age": int(parts[1]), "email": parts[2]}


class DataProcessor:
    """Processes numerical data items."""

    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def process(self) -> list:
        """Returns a list with all elements doubled."""
        return [item * 2 for item in self.data]
