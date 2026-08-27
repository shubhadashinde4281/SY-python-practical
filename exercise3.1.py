
age = int(input("Enter your age: "))
income = float(input("Enter your annual family income: "))

if age < 25 and income < 300000:
    print("\nCongratulations!")
    print("You are eligible for the scholarship.")
else:
    print("\nSorry!")
    print("You are not eligible for the scholarship.")