mark = int(input("Enter your mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 90:
    print("A grade")
elif mark >= 75:
    print("B grade")
elif mark >= 50:
    print("C grade")
else:
    print("Failed")
