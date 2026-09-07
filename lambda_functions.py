"""Examples of map, filter, and reduce."""
# Lambdas are small one-line functions used here for practice.
from functools import reduce


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Squares:", list(map(lambda number: number**2, numbers)))
    print("Even numbers:", list(filter(lambda number: number % 2 == 0, numbers)))
    print("Product:", reduce(lambda left, right: left * right, numbers))
