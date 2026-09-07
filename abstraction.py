"""A small abstraction example."""
# Abstract base classes define a required method for all vehicle types.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self) -> str:
        """Start the vehicle."""


class Bike(Vehicle):
    def start(self) -> str:
        return "Bike is starting."


if __name__ == "__main__":
    print(Bike().start())
