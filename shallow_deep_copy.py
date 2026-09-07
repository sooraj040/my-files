"""Compare shallow and deep copies."""
# A shallow copy shares nested lists; a deep copy creates independent nested lists.
from copy import copy, deepcopy


if __name__ == "__main__":
    original = [[10, 15, 20]]
    shallow, deep = copy(original), deepcopy(original)
    original[0][0] = 99
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)
