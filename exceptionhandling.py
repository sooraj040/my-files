try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print("Result:", numerator / denominator)
except ValueError:
    print("Please enter whole numbers.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Program completed without errors.")
finally:
    print("Program finished.")
