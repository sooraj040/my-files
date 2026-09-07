count = int(input("Enter the number of terms: "))
first = 0
second = 1

for i in range(count):
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number
