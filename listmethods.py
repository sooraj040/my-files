people = []
answer = "y"

while answer == "y":
    name = input("Name: ")
    age = input("Age: ")
    people.append([name, age])
    answer = input("Add another person? (y/n): ").lower()

print("Final list:", people)
