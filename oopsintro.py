"""Class and instance method example."""
# `institute` belongs to the class, while name and place belong to each student.


class Student:
    institute = "One Team"

    def __init__(self, name: str, place: str) -> None:
        self.name, self.place = name, place

    def introduction(self) -> str:
        return f"Hello {self.name}, welcome to {self.institute}. You are from {self.place}."


if __name__ == "__main__":
    print(Student("Ebin", "Vypin").introduction())
