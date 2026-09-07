n = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= n:
    factorial = factorial * i
    i = i + 1

i = n
calculation = ""

while i >= 1:
    calculation = calculation + str(i)
    if i > 1:
        calculation = calculation + " x "
    i = i - 1

print(calculation, "=", factorial)
print("Factorial =", factorial)
