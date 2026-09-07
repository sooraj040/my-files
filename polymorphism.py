"""Polymorphism example."""
# `display_students` works with any Team subclass that provides `students()`.


class Team:
    def students(self) -> list[str]:
        return []


class BatchOne(Team):
    def students(self) -> list[str]:
        return ["Adwin", "Sooraj"]


def display_students(team: Team) -> None:
    print(*team.students(), sep="\n")


if __name__ == "__main__":
    display_students(BatchOne())
