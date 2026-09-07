"""Encapsulation using properties."""
# A property exposes read-only access to the protected `_name` attribute.


class Animal:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self._breed = breed

    def get_info(self) -> str:
        return f"{self.name} is a {self._breed}."


if __name__ == "__main__":
    print(Dog("Buddy", "Golden Retriever").get_info())
