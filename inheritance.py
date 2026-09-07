"""Inheritance example."""
# Dog inherits the `name` attribute from Animal and adds its own behavior.


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def introduce(self) -> str:
        return f"My name is {self.name}."


if __name__ == "__main__":
    print(Dog("Ricky").introduce())
