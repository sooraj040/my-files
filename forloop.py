"""Multiplication table using a for loop."""
# The comprehension builds one formatted line for each multiplier from 1 to 10.


number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
