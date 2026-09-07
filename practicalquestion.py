text = "hello"
count = {}

for character in text:
    if character in count:
        count[character] = count[character] + 1
    else:
        count[character] = 1

print(count)

numbers = [19, 2, 1, 23, 8]

for end in range(len(numbers) - 1, 0, -1):
    for index in range(end):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

print(numbers)
